import streamlit as st
import pandas as pd
import math
from scipy.stats import chi2


# =========================================================================
# PAGE CONFIG — sidebar stays expanded/fixed on left by default
# =========================================================================

st.set_page_config(
    page_title="IT Sector Portfolio VaR & ES Analysis",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================================
# PAGE TITLE
# =========================================================================

st.title("IT Sector Portfolio VaR & ES Analysis")

st.write(
    "Historical and Parametric VaR, Expected Shortfall and Kupiec Backtesting"
)


# =========================================================================
# LOAD DATA
# =========================================================================

df = pd.read_excel("data/Portfolio_Returns_Merged.xlsx")

return_columns = [
    'TCS_Day_Return', 'COFORGE_Day_Return', 'HCLTECH_Day_Return',
    'INFY_Day_Return', 'LTM_Day_Return', 'LTTS_Day_Return',
    'MPHASIS_Day_Return', 'PERSISTENT_Day_Return', 'TECHM_Day_Return',
    'WIPRO_Day_Return',

    'TCS_5Day_Return', 'COFORGE_5Day_Return', 'HCLTECH_5Day_Return',
    'INFY_5Day_Return', 'LTM_5Day_Return', 'LTTS_5Day_Return',
    'MPHASIS_5Day_Return', 'PERSISTENT_5Day_Return', 'TECHM_5Day_Return',
    'WIPRO_5Day_Return',

    'TCS_30Day_Return', 'COFORGE_30Day_Return', 'HCLTECH_30Day_Return',
    'INFY_30Day_Return', 'LTM_30Day_Return', 'LTTS_30Day_Return',
    'MPHASIS_30Day_Return', 'PERSISTENT_30Day_Return', 'TECHM_30Day_Return',
    'WIPRO_30Day_Return',

    'TCS_90Day_Return', 'COFORGE_90Day_Return', 'HCLTECH_90Day_Return',
    'INFY_90Day_Return', 'LTM_90Day_Return', 'LTTS_90Day_Return',
    'MPHASIS_90Day_Return', 'PERSISTENT_90Day_Return', 'TECHM_90Day_Return',
    'WIPRO_90Day_Return'
]

for column in return_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# =========================================================================
# CORRELATION MATRIX
# =========================================================================

correlation_matrix = df[
    [
        'TCS_Day_Return',
        'COFORGE_Day_Return',
        'HCLTECH_Day_Return',
        'INFY_Day_Return',
        'LTM_Day_Return',
        'LTTS_Day_Return',
        'MPHASIS_Day_Return',
        'PERSISTENT_Day_Return',
        'TECHM_Day_Return',
        'WIPRO_Day_Return'
    ]
].corr()


# =========================================================================
# COVARIANCE MATRIX
# =========================================================================

covariance_matrix = df[
    [
        'TCS_Day_Return',
        'COFORGE_Day_Return',
        'HCLTECH_Day_Return',
        'INFY_Day_Return',
        'LTM_Day_Return',
        'LTTS_Day_Return',
        'MPHASIS_Day_Return',
        'PERSISTENT_Day_Return',
        'TECHM_Day_Return',
        'WIPRO_Day_Return'
    ]
].cov()


# =========================================================================
# SIDEBAR — SIMPLE TEXT INVESTMENT INPUT (no stepper/slider buttons)
# =========================================================================

st.sidebar.header("Portfolio Investment")
st.sidebar.write("Enter the amount to invest in each stock (₹)")

tcs_input = st.sidebar.text_input("TCS", value="100000")
coforge_input = st.sidebar.text_input("COFORGE", value="100000")
hcltech_input = st.sidebar.text_input("HCLTECH", value="100000")
infy_input = st.sidebar.text_input("INFY", value="100000")
ltm_input = st.sidebar.text_input("LTM", value="100000")
lt_input = st.sidebar.text_input("LTTS", value="100000")
mphasis_input = st.sidebar.text_input("MPHASIS", value="100000")
persistent_input = st.sidebar.text_input("PERSISTENT", value="100000")
techm_input = st.sidebar.text_input("TECHM", value="100000")
wipro_input = st.sidebar.text_input("WIPRO", value="100000")


# =========================================================================
# CONVERT TEXT INPUT TO NUMBERS (with basic validation)
# =========================================================================

def parse_amount(value, label):
    try:
        amount = float(value)
        if amount < 0:
            st.sidebar.error(f"{label}: amount cannot be negative")
            return 0.0
        return amount
    except ValueError:
        st.sidebar.error(f"{label}: please enter a valid number")
        return 0.0


tcs = parse_amount(tcs_input, "TCS")
coforge = parse_amount(coforge_input, "COFORGE")
hcltech = parse_amount(hcltech_input, "HCLTECH")
infy = parse_amount(infy_input, "INFY")
ltm = parse_amount(ltm_input, "LTM")
lt = parse_amount(lt_input, "LTTS")
mphasis = parse_amount(mphasis_input, "MPHASIS")
persistent = parse_amount(persistent_input, "PERSISTENT")
techm = parse_amount(techm_input, "TECHM")
wipro = parse_amount(wipro_input, "WIPRO")

total_investment = (
    tcs + coforge + hcltech + infy + ltm + lt + mphasis + persistent + techm + wipro
)

st.sidebar.markdown("---")
st.sidebar.metric(
    label="Total Investment",
    value=f"₹{total_investment:,.2f}"
)


# =========================================================================
# TOTAL INVESTMENT (main page)
# =========================================================================

st.metric(
    label="Total Portfolio Investment",
    value=f"₹{total_investment:,.2f}"
)


# =========================================================================
# PORTFOLIO WEIGHTS + EVERYTHING ELSE
# =========================================================================

if total_investment > 0:

    tcs_weight = tcs / total_investment
    coforge_weight = coforge / total_investment
    hcltech_weight = hcltech / total_investment
    infy_weight = infy / total_investment
    ltm_weight = ltm / total_investment
    lt_weight = lt / total_investment
    mphasis_weight = mphasis / total_investment
    persistent_weight = persistent / total_investment
    techm_weight = techm / total_investment
    wipro_weight = wipro / total_investment


    # =========================================================================
    # PORTFOLIO RETURN — 1 DAY
    # =========================================================================

    return_tcs = df['TCS_Day_Return'] * tcs
    return_coforge = df['COFORGE_Day_Return'] * coforge
    return_hcltech = df['HCLTECH_Day_Return'] * hcltech
    return_infy = df['INFY_Day_Return'] * infy
    return_ltm = df['LTM_Day_Return'] * ltm
    return_lt = df['LTTS_Day_Return'] * lt
    return_mphasis = df['MPHASIS_Day_Return'] * mphasis
    return_persistent = df['PERSISTENT_Day_Return'] * persistent
    return_techm = df['TECHM_Day_Return'] * techm
    return_wipro = df['WIPRO_Day_Return'] * wipro

    portfolio_return = (
        return_tcs + return_coforge + return_hcltech + return_infy + return_ltm +
        return_lt + return_mphasis + return_persistent + return_techm + return_wipro
    ) / total_investment


    # =========================================================================
    # PORTFOLIO RETURN — 5 DAY
    # =========================================================================

    return_tcs_5day = df['TCS_5Day_Return'] * tcs
    return_coforge_5day = df['COFORGE_5Day_Return'] * coforge
    return_hcltech_5day = df['HCLTECH_5Day_Return'] * hcltech
    return_infy_5day = df['INFY_5Day_Return'] * infy
    return_ltm_5day = df['LTM_5Day_Return'] * ltm
    return_lt_5day = df['LTTS_5Day_Return'] * lt
    return_mphasis_5day = df['MPHASIS_5Day_Return'] * mphasis
    return_persistent_5day = df['PERSISTENT_5Day_Return'] * persistent
    return_techm_5day = df['TECHM_5Day_Return'] * techm
    return_wipro_5day = df['WIPRO_5Day_Return'] * wipro

    portfolio_5day_return = (
        return_tcs_5day + return_coforge_5day + return_hcltech_5day + return_infy_5day +
        return_ltm_5day + return_lt_5day + return_mphasis_5day + return_persistent_5day +
        return_techm_5day + return_wipro_5day
    ) / total_investment


    # =========================================================================
    # PORTFOLIO RETURN — 30 DAY
    # =========================================================================

    return_tcs_30day = df['TCS_30Day_Return'] * tcs
    return_coforge_30day = df['COFORGE_30Day_Return'] * coforge
    return_hcltech_30day = df['HCLTECH_30Day_Return'] * hcltech
    return_infy_30day = df['INFY_30Day_Return'] * infy
    return_ltm_30day = df['LTM_30Day_Return'] * ltm
    return_lt_30day = df['LTTS_30Day_Return'] * lt
    return_mphasis_30day = df['MPHASIS_30Day_Return'] * mphasis
    return_persistent_30day = df['PERSISTENT_30Day_Return'] * persistent
    return_techm_30day = df['TECHM_30Day_Return'] * techm
    return_wipro_30day = df['WIPRO_30Day_Return'] * wipro

    portfolio_30day_return = (
        return_tcs_30day + return_coforge_30day + return_hcltech_30day + return_infy_30day +
        return_ltm_30day + return_lt_30day + return_mphasis_30day + return_persistent_30day +
        return_techm_30day + return_wipro_30day
    ) / total_investment


    # =========================================================================
    # PORTFOLIO RETURN — 90 DAY
    # =========================================================================

    return_tcs_90day = df['TCS_90Day_Return'] * tcs
    return_coforge_90day = df['COFORGE_90Day_Return'] * coforge
    return_hcltech_90day = df['HCLTECH_90Day_Return'] * hcltech
    return_infy_90day = df['INFY_90Day_Return'] * infy
    return_ltm_90day = df['LTM_90Day_Return'] * ltm
    return_lt_90day = df['LTTS_90Day_Return'] * lt
    return_mphasis_90day = df['MPHASIS_90Day_Return'] * mphasis
    return_persistent_90day = df['PERSISTENT_90Day_Return'] * persistent
    return_techm_90day = df['TECHM_90Day_Return'] * techm
    return_wipro_90day = df['WIPRO_90Day_Return'] * wipro

    portfolio_90day_return = (
        return_tcs_90day + return_coforge_90day + return_hcltech_90day + return_infy_90day +
        return_ltm_90day + return_lt_90day + return_mphasis_90day + return_persistent_90day +
        return_techm_90day + return_wipro_90day
    ) / total_investment


    # =========================================================================
    # HISTORICAL VaR
    # =========================================================================

    historical_var_1day_95 = portfolio_return.quantile(0.05)
    historical_var_1day_99 = portfolio_return.quantile(0.01)

    historical_var_5day_95 = portfolio_5day_return.quantile(0.05)
    historical_var_5day_99 = portfolio_5day_return.quantile(0.01)

    historical_var_30day_95 = portfolio_30day_return.quantile(0.05)
    historical_var_30day_99 = portfolio_30day_return.quantile(0.01)

    historical_var_90day_95 = portfolio_90day_return.quantile(0.05)
    historical_var_90day_99 = portfolio_90day_return.quantile(0.01)


    # =========================================================================
    # HISTORICAL ES / CVaR
    # =========================================================================

    tail_returns_1day_95 = portfolio_return[portfolio_return <= historical_var_1day_95]
    tail_returns_1day_99 = portfolio_return[portfolio_return <= historical_var_1day_99]
    cvar_1day_95 = tail_returns_1day_95.mean()
    cvar_1day_99 = tail_returns_1day_99.mean()

    tail_returns_5day_95 = portfolio_5day_return[portfolio_5day_return <= historical_var_5day_95]
    tail_returns_5day_99 = portfolio_5day_return[portfolio_5day_return <= historical_var_5day_99]
    cvar_5day_95 = tail_returns_5day_95.mean()
    cvar_5day_99 = tail_returns_5day_99.mean()

    tail_returns_30day_95 = portfolio_30day_return[portfolio_30day_return <= historical_var_30day_95]
    tail_returns_30day_99 = portfolio_30day_return[portfolio_30day_return <= historical_var_30day_99]
    cvar_30day_95 = tail_returns_30day_95.mean()
    cvar_30day_99 = tail_returns_30day_99.mean()

    tail_returns_90day_95 = portfolio_90day_return[portfolio_90day_return <= historical_var_90day_95]
    tail_returns_90day_99 = portfolio_90day_return[portfolio_90day_return <= historical_var_90day_99]
    cvar_90day_95 = tail_returns_90day_95.mean()
    cvar_90day_99 = tail_returns_90day_99.mean()


    # =========================================================================
    # PORTFOLIO STATISTICS
    # =========================================================================

    portfolio_mean = portfolio_return.mean()
    portfolio_variance = portfolio_return.var()
    portfolio_std_dev = portfolio_return.std()
    annualized_volatility = portfolio_std_dev * (252 ** 0.5)

    portfolio_mean_5day = portfolio_5day_return.mean()
    portfolio_variance_5day = portfolio_5day_return.var()
    portfolio_std_dev_5day = portfolio_5day_return.std()
    annualized_volatility_5day = portfolio_std_dev_5day * ((252 / 5) ** 0.5)

    portfolio_mean_30day = portfolio_30day_return.mean()
    portfolio_variance_30day = portfolio_30day_return.var()
    portfolio_std_dev_30day = portfolio_30day_return.std()
    annualized_volatility_30day = portfolio_std_dev_30day * ((252 / 30) ** 0.5)

    portfolio_mean_90day = portfolio_90day_return.mean()
    portfolio_variance_90day = portfolio_90day_return.var()
    portfolio_std_dev_90day = portfolio_90day_return.std()
    annualized_volatility_90day = portfolio_std_dev_90day * ((252 / 90) ** 0.5)


    # =========================================================================
    # PARAMETRIC VaR
    # =========================================================================

    z95 = 1.65
    z99 = 2.33

    param_var_1day_95 = portfolio_mean - z95 * portfolio_std_dev
    param_var_1day_99 = portfolio_mean - z99 * portfolio_std_dev

    param_var_5day_95 = portfolio_mean_5day - z95 * portfolio_std_dev_5day
    param_var_5day_99 = portfolio_mean_5day - z99 * portfolio_std_dev_5day

    param_var_30day_95 = portfolio_mean_30day - z95 * portfolio_std_dev_30day
    param_var_30day_99 = portfolio_mean_30day - z99 * portfolio_std_dev_30day

    param_var_90day_95 = portfolio_mean_90day - z95 * portfolio_std_dev_90day
    param_var_90day_99 = portfolio_mean_90day - z99 * portfolio_std_dev_90day


    # =========================================================================
    # PARAMETRIC ES / CVaR
    # =========================================================================

    confidence_95 = 0.95
    confidence_99 = 0.99

    es_1_95 = (portfolio_mean - portfolio_std_dev * (math.exp(-(z95 ** 2) / 2) / ((1 - confidence_95) * math.sqrt(2 * math.pi))))
    es_1_99 = (portfolio_mean - portfolio_std_dev * (math.exp(-(z99 ** 2) / 2) / ((1 - confidence_99) * math.sqrt(2 * math.pi))))

    es_5_95 = (portfolio_mean_5day - portfolio_std_dev_5day * (math.exp(-(z95 ** 2) / 2) / ((1 - confidence_95) * math.sqrt(2 * math.pi))))
    es_5_99 = (portfolio_mean_5day - portfolio_std_dev_5day * (math.exp(-(z99 ** 2) / 2) / ((1 - confidence_99) * math.sqrt(2 * math.pi))))

    es_30_95 = (portfolio_mean_30day - portfolio_std_dev_30day * (math.exp(-(z95 ** 2) / 2) / ((1 - confidence_95) * math.sqrt(2 * math.pi))))
    es_30_99 = (portfolio_mean_30day - portfolio_std_dev_30day * (math.exp(-(z99 ** 2) / 2) / ((1 - confidence_99) * math.sqrt(2 * math.pi))))

    es_90_95 = (portfolio_mean_90day - portfolio_std_dev_90day * (math.exp(-(z95 ** 2) / 2) / ((1 - confidence_95) * math.sqrt(2 * math.pi))))
    es_90_99 = (portfolio_mean_90day - portfolio_std_dev_90day * (math.exp(-(z99 ** 2) / 2) / ((1 - confidence_99) * math.sqrt(2 * math.pi))))


    # =========================================================================
    # STAGE 1 — HISTORICAL VaR BACKTESTING
    # =========================================================================

    historical_breach_1day_95 = portfolio_return < historical_var_1day_95
    historical_breaches_1day_95 = historical_breach_1day_95.sum()
    total_observations_1day = portfolio_return.notna().sum()
    historical_breach_rate_1day_95 = historical_breaches_1day_95 / total_observations_1day

    historical_breach_1day_99 = portfolio_return < historical_var_1day_99
    historical_breaches_1day_99 = historical_breach_1day_99.sum()
    historical_breach_rate_1day_99 = historical_breaches_1day_99 / total_observations_1day

    historical_breach_5day_95 = portfolio_5day_return < historical_var_5day_95
    historical_breaches_5day_95 = historical_breach_5day_95.sum()
    total_observations_5day = portfolio_5day_return.notna().sum()
    historical_breach_rate_5day_95 = historical_breaches_5day_95 / total_observations_5day

    historical_breach_5day_99 = portfolio_5day_return < historical_var_5day_99
    historical_breaches_5day_99 = historical_breach_5day_99.sum()
    historical_breach_rate_5day_99 = historical_breaches_5day_99 / total_observations_5day

    historical_breach_30day_95 = portfolio_30day_return < historical_var_30day_95
    historical_breaches_30day_95 = historical_breach_30day_95.sum()
    total_observations_30day = portfolio_30day_return.notna().sum()
    historical_breach_rate_30day_95 = historical_breaches_30day_95 / total_observations_30day

    historical_breach_30day_99 = portfolio_30day_return < historical_var_30day_99
    historical_breaches_30day_99 = historical_breach_30day_99.sum()
    historical_breach_rate_30day_99 = historical_breaches_30day_99 / total_observations_30day

    historical_breach_90day_95 = portfolio_90day_return < historical_var_90day_95
    historical_breaches_90day_95 = historical_breach_90day_95.sum()
    total_observations_90day = portfolio_90day_return.notna().sum()
    historical_breach_rate_90day_95 = historical_breaches_90day_95 / total_observations_90day

    historical_breach_90day_99 = portfolio_90day_return < historical_var_90day_99
    historical_breaches_90day_99 = historical_breach_90day_99.sum()
    historical_breach_rate_90day_99 = historical_breaches_90day_99 / total_observations_90day


    # =========================================================================
    # STAGE 1 — PARAMETRIC VaR BACKTESTING
    # =========================================================================

    parametric_breach_1day_95 = portfolio_return < param_var_1day_95
    parametric_breaches_1day_95 = parametric_breach_1day_95.sum()
    parametric_breach_rate_1day_95 = parametric_breaches_1day_95 / total_observations_1day

    parametric_breach_1day_99 = portfolio_return < param_var_1day_99
    parametric_breaches_1day_99 = parametric_breach_1day_99.sum()
    parametric_breach_rate_1day_99 = parametric_breaches_1day_99 / total_observations_1day

    parametric_breach_5day_95 = portfolio_5day_return < param_var_5day_95
    parametric_breaches_5day_95 = parametric_breach_5day_95.sum()
    parametric_breach_rate_5day_95 = parametric_breaches_5day_95 / total_observations_5day

    parametric_breach_5day_99 = portfolio_5day_return < param_var_5day_99
    parametric_breaches_5day_99 = parametric_breach_5day_99.sum()
    parametric_breach_rate_5day_99 = parametric_breaches_5day_99 / total_observations_5day

    parametric_breach_30day_95 = portfolio_30day_return < param_var_30day_95
    parametric_breaches_30day_95 = parametric_breach_30day_95.sum()
    parametric_breach_rate_30day_95 = parametric_breaches_30day_95 / total_observations_30day

    parametric_breach_30day_99 = portfolio_30day_return < param_var_30day_99
    parametric_breaches_30day_99 = parametric_breach_30day_99.sum()
    parametric_breach_rate_30day_99 = parametric_breaches_30day_99 / total_observations_30day

    parametric_breach_90day_95 = portfolio_90day_return < param_var_90day_95
    parametric_breaches_90day_95 = parametric_breach_90day_95.sum()
    parametric_breach_rate_90day_95 = parametric_breaches_90day_95 / total_observations_90day

    parametric_breach_90day_99 = portfolio_90day_return < param_var_90day_99
    parametric_breaches_90day_99 = parametric_breach_90day_99.sum()
    parametric_breach_rate_90day_99 = parametric_breaches_90day_99 / total_observations_90day


    # =========================================================================
    # STAGE 2 — KUPIEC POF TEST
    # =========================================================================

    def kupiec_test(breaches, observations, confidence):
        p = 1 - confidence
        n = breaches
        t = observations
        phat = n / t

        if n == 0:
            lr_pof = -2 * ((t - n) * math.log(1 - p) - (t - n) * math.log(1 - phat))
        elif n == t:
            lr_pof = -2 * (n * math.log(p) - n * math.log(phat))
        else:
            lr_pof = -2 * (
                (t - n) * math.log(1 - p) + n * math.log(p)
                - (t - n) * math.log(1 - phat) - n * math.log(phat)
            )

        p_value = 1 - chi2.cdf(lr_pof, 1)
        result = "PASS" if p_value > 0.05 else "FAIL"
        return lr_pof, p_value, result


    # =========================================================================
    # HISTORICAL KUPIEC TESTS
    # =========================================================================

    historical_kupiec_1day_95 = kupiec_test(historical_breaches_1day_95, total_observations_1day, 0.95)
    historical_kupiec_1day_99 = kupiec_test(historical_breaches_1day_99, total_observations_1day, 0.99)
    historical_kupiec_5day_95 = kupiec_test(historical_breaches_5day_95, total_observations_5day, 0.95)
    historical_kupiec_5day_99 = kupiec_test(historical_breaches_5day_99, total_observations_5day, 0.99)
    historical_kupiec_30day_95 = kupiec_test(historical_breaches_30day_95, total_observations_30day, 0.95)
    historical_kupiec_30day_99 = kupiec_test(historical_breaches_30day_99, total_observations_30day, 0.99)
    historical_kupiec_90day_95 = kupiec_test(historical_breaches_90day_95, total_observations_90day, 0.95)
    historical_kupiec_90day_99 = kupiec_test(historical_breaches_90day_99, total_observations_90day, 0.99)


    # =========================================================================
    # PARAMETRIC KUPIEC TESTS
    # =========================================================================

    parametric_kupiec_1day_95 = kupiec_test(parametric_breaches_1day_95, total_observations_1day, 0.95)
    parametric_kupiec_1day_99 = kupiec_test(parametric_breaches_1day_99, total_observations_1day, 0.99)
    parametric_kupiec_5day_95 = kupiec_test(parametric_breaches_5day_95, total_observations_5day, 0.95)
    parametric_kupiec_5day_99 = kupiec_test(parametric_breaches_5day_99, total_observations_5day, 0.99)
    parametric_kupiec_30day_95 = kupiec_test(parametric_breaches_30day_95, total_observations_30day, 0.95)
    parametric_kupiec_30day_99 = kupiec_test(parametric_breaches_30day_99, total_observations_30day, 0.99)
    parametric_kupiec_90day_95 = kupiec_test(parametric_breaches_90day_95, total_observations_90day, 0.95)
    parametric_kupiec_90day_99 = kupiec_test(parametric_breaches_90day_99, total_observations_90day, 0.99)


    # =========================================================================
    # DISPLAY PORTFOLIO WEIGHTS
    # =========================================================================

    st.header("Portfolio Allocation")

    weights = pd.DataFrame(
        {
            "Stock": ["TCS", "COFORGE", "HCLTECH", "INFY", "LTM", "LTTS", "MPHASIS", "PERSISTENT", "TECHM", "WIPRO"],
            "Investment": [tcs, coforge, hcltech, infy, ltm, lt, mphasis, persistent, techm, wipro],
            "Weight": [tcs_weight, coforge_weight, hcltech_weight, infy_weight, ltm_weight,
                       lt_weight, mphasis_weight, persistent_weight, techm_weight, wipro_weight]
        }
    )

    weights["Weight"] = weights["Weight"].map(lambda x: f"{x:.2%}")

    st.dataframe(
        weights.style.format({"Investment": "₹{:,.2f}"}),
        use_container_width=True
    )


    # =========================================================================
    # PORTFOLIO STATISTICS
    # =========================================================================

    st.header("Portfolio Statistics")

    statistics = pd.DataFrame(
        {
            "Horizon": ["1 Day", "5 Day", "30 Day", "90 Day"],
            "Mean": [portfolio_mean, portfolio_mean_5day, portfolio_mean_30day, portfolio_mean_90day],
            "Variance": [portfolio_variance, portfolio_variance_5day, portfolio_variance_30day, portfolio_variance_90day],
            "Standard Deviation": [portfolio_std_dev, portfolio_std_dev_5day, portfolio_std_dev_30day, portfolio_std_dev_90day],
            "Annualized Volatility": [annualized_volatility, annualized_volatility_5day, annualized_volatility_30day, annualized_volatility_90day]
        }
    )

    st.dataframe(
        statistics.style.format(
            {
                "Mean": "{:.4%}",
                "Variance": "{:.6f}",
                "Standard Deviation": "{:.4%}",
                "Annualized Volatility": "{:.2%}"
            }
        ),
        use_container_width=True
    )


    # =========================================================================
    # VaR RESULTS
    # =========================================================================

    st.header("VaR Results")

    var_results = pd.DataFrame(
        {
            "Horizon": ["1 Day", "5 Day", "30 Day", "90 Day"],
            "Historical VaR 95%": [historical_var_1day_95, historical_var_5day_95, historical_var_30day_95, historical_var_90day_95],
            "Historical VaR 99%": [historical_var_1day_99, historical_var_5day_99, historical_var_30day_99, historical_var_90day_99],
            "Parametric VaR 95%": [param_var_1day_95, param_var_5day_95, param_var_30day_95, param_var_90day_95],
            "Parametric VaR 99%": [param_var_1day_99, param_var_5day_99, param_var_30day_99, param_var_90day_99]
        }
    )

    st.dataframe(
        var_results.style.format(
            {
                "Historical VaR 95%": "{:.4%}",
                "Historical VaR 99%": "{:.4%}",
                "Parametric VaR 95%": "{:.4%}",
                "Parametric VaR 99%": "{:.4%}"
            }
        ),
        use_container_width=True
    )

    st.subheader("VaR Comparison")
    var_chart = var_results.set_index("Horizon")[
        ["Historical VaR 95%", "Historical VaR 99%", "Parametric VaR 95%", "Parametric VaR 99%"]
    ]
    st.bar_chart(var_chart)


    # =========================================================================
    # ES RESULTS
    # =========================================================================

    st.header("Expected Shortfall / CVaR")

    es_results = pd.DataFrame(
        {
            "Horizon": ["1 Day", "5 Day", "30 Day", "90 Day"],
            "Historical ES 95%": [cvar_1day_95, cvar_5day_95, cvar_30day_95, cvar_90day_95],
            "Historical ES 99%": [cvar_1day_99, cvar_5day_99, cvar_30day_99, cvar_90day_99],
            "Parametric ES 95%": [es_1_95, es_5_95, es_30_95, es_90_95],
            "Parametric ES 99%": [es_1_99, es_5_99, es_30_99, es_90_99]
        }
    )

    st.dataframe(
        es_results.style.format(
            {
                "Historical ES 95%": "{:.4%}",
                "Historical ES 99%": "{:.4%}",
                "Parametric ES 95%": "{:.4%}",
                "Parametric ES 99%": "{:.4%}"
            }
        ),
        use_container_width=True
    )

    st.subheader("Expected Shortfall Comparison")
    es_chart = es_results.set_index("Horizon")[
        ["Historical ES 95%", "Historical ES 99%", "Parametric ES 95%", "Parametric ES 99%"]
    ]
    st.bar_chart(es_chart)


    # =========================================================================
    # STAGE 1 — BREACH ANALYSIS
    # =========================================================================

    st.header("VaR Breach Analysis")

    breach_results = pd.DataFrame(
        {
            "Method": ["Historical"] * 8 + ["Parametric"] * 8,
            "Horizon": ["1 Day", "1 Day", "5 Day", "5 Day", "30 Day", "30 Day", "90 Day", "90 Day"] * 2,
            "Confidence": ["95%", "99%"] * 8,
            "Breaches": [
                historical_breaches_1day_95, historical_breaches_1day_99,
                historical_breaches_5day_95, historical_breaches_5day_99,
                historical_breaches_30day_95, historical_breaches_30day_99,
                historical_breaches_90day_95, historical_breaches_90day_99,
                parametric_breaches_1day_95, parametric_breaches_1day_99,
                parametric_breaches_5day_95, parametric_breaches_5day_99,
                parametric_breaches_30day_95, parametric_breaches_30day_99,
                parametric_breaches_90day_95, parametric_breaches_90day_99
            ],
            "Observations": [
                total_observations_1day, total_observations_1day,
                total_observations_5day, total_observations_5day,
                total_observations_30day, total_observations_30day,
                total_observations_90day, total_observations_90day,
                total_observations_1day, total_observations_1day,
                total_observations_5day, total_observations_5day,
                total_observations_30day, total_observations_30day,
                total_observations_90day, total_observations_90day
            ],
            "Actual Breach Rate": [
                historical_breach_rate_1day_95, historical_breach_rate_1day_99,
                historical_breach_rate_5day_95, historical_breach_rate_5day_99,
                historical_breach_rate_30day_95, historical_breach_rate_30day_99,
                historical_breach_rate_90day_95, historical_breach_rate_90day_99,
                parametric_breach_rate_1day_95, parametric_breach_rate_1day_99,
                parametric_breach_rate_5day_95, parametric_breach_rate_5day_99,
                parametric_breach_rate_30day_95, parametric_breach_rate_30day_99,
                parametric_breach_rate_90day_95, parametric_breach_rate_90day_99
            ],
            "Expected Breach Rate": [0.05, 0.01] * 8
        }
    )

    st.dataframe(
        breach_results.style.format(
            {"Actual Breach Rate": "{:.2%}", "Expected Breach Rate": "{:.2%}"}
        ),
        use_container_width=True
    )

    st.subheader("VaR Breach Rate Comparison")
    breach_chart = breach_results.set_index("Horizon")[["Actual Breach Rate", "Expected Breach Rate"]]
    st.bar_chart(breach_chart)


    # =========================================================================
    # STAGE 2 — KUPIEC POF
    # =========================================================================

    st.header("Kupiec POF Backtesting")

    kupiec_results = pd.DataFrame(
        {
            "Method": ["Historical"] * 8 + ["Parametric"] * 8,
            "Horizon": ["1 Day", "1 Day", "5 Day", "5 Day", "30 Day", "30 Day", "90 Day", "90 Day"] * 2,
            "Confidence": ["95%", "99%"] * 8,
            "LR POF": [
                historical_kupiec_1day_95[0], historical_kupiec_1day_99[0],
                historical_kupiec_5day_95[0], historical_kupiec_5day_99[0],
                historical_kupiec_30day_95[0], historical_kupiec_30day_99[0],
                historical_kupiec_90day_95[0], historical_kupiec_90day_99[0],
                parametric_kupiec_1day_95[0], parametric_kupiec_1day_99[0],
                parametric_kupiec_5day_95[0], parametric_kupiec_5day_99[0],
                parametric_kupiec_30day_95[0], parametric_kupiec_30day_99[0],
                parametric_kupiec_90day_95[0], parametric_kupiec_90day_99[0]
            ],
            "P-Value": [
                historical_kupiec_1day_95[1], historical_kupiec_1day_99[1],
                historical_kupiec_5day_95[1], historical_kupiec_5day_99[1],
                historical_kupiec_30day_95[1], historical_kupiec_30day_99[1],
                historical_kupiec_90day_95[1], historical_kupiec_90day_99[1],
                parametric_kupiec_1day_95[1], parametric_kupiec_1day_99[1],
                parametric_kupiec_5day_95[1], parametric_kupiec_5day_99[1],
                parametric_kupiec_30day_95[1], parametric_kupiec_30day_99[1],
                parametric_kupiec_90day_95[1], parametric_kupiec_90day_99[1]
            ],
            "Result": [
                historical_kupiec_1day_95[2], historical_kupiec_1day_99[2],
                historical_kupiec_5day_95[2], historical_kupiec_5day_99[2],
                historical_kupiec_30day_95[2], historical_kupiec_30day_99[2],
                historical_kupiec_90day_95[2], historical_kupiec_90day_99[2],
                parametric_kupiec_1day_95[2], parametric_kupiec_1day_99[2],
                parametric_kupiec_5day_95[2], parametric_kupiec_5day_99[2],
                parametric_kupiec_30day_95[2], parametric_kupiec_30day_99[2],
                parametric_kupiec_90day_95[2], parametric_kupiec_90day_99[2]
            ]
        }
    )

    st.dataframe(
        kupiec_results.style.format({"LR POF": "{:.6f}", "P-Value": "{:.6f}"}),
        use_container_width=True
    )


    # =========================================================================
    # CORRELATION MATRIX
    # =========================================================================

    st.header("Stock Return Correlation Matrix")
    st.dataframe(correlation_matrix.style.format("{:.3f}"), use_container_width=True)


    # =========================================================================
    # COVARIANCE MATRIX
    # =========================================================================

    st.header("Stock Return Covariance Matrix")
    st.dataframe(covariance_matrix.style.format("{:.6f}"), use_container_width=True)


    # =========================================================================
    # FULL UNDERLYING DATASET
    # =========================================================================

    st.header("Underlying Dataset")
    st.write(f"Dataset contains {df.shape[0]:,} rows and {df.shape[1]:,} columns.")
    st.dataframe(df, use_container_width=True, height=600)


else:
    st.warning("Please enter at least some investment amount.")