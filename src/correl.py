import pandas as pd
import math
from scipy.stats import chi2

df = pd.read_excel(r"D:\IT QUANT\PROJECTS\var es project\data\Portfolio_Returns_Merged.xlsx")

# correlation matrix
correlation_matrix = df[['TCS_Day_Return', 'COFORGE_Day_Return', 'HCLTECH_Day_Return', 'INFY_Day_Return',
                          'LTM_Day_Return', 'LTTS_Day_Return', 'MPHASIS_Day_Return', 'PERSISTENT_Day_Return',
                          'TECHM_Day_Return', 'WIPRO_Day_Return']].corr()

# covariance matrix
covariance_matrix = df[['TCS_Day_Return', 'COFORGE_Day_Return', 'HCLTECH_Day_Return', 'INFY_Day_Return',
                         'LTM_Day_Return', 'LTTS_Day_Return', 'MPHASIS_Day_Return', 'PERSISTENT_Day_Return',
                         'TECHM_Day_Return', 'WIPRO_Day_Return']].cov()


# =========================================================================
# PORTFOLIO RETURN — START
# =========================================================================

tcs = float(input("Enter the amount to invest in TCS: "))
coforge = float(input("Enter the amount to invest in COFORGE: "))
hcltech = float(input("Enter the amount to invest in HCLTECH: "))
infy = float(input("Enter the amount to invest in INFY: "))
ltm = float(input("Enter the amount to invest in LTM: "))
lt = float(input("Enter the amount to invest in LTTS: "))
mphasis = float(input("Enter the amount to invest in MPHASIS: "))
persistent = float(input("Enter the amount to invest in PERSISTENT: "))
techm = float(input("Enter the amount to invest in TECHM: "))
wipro = float(input("Enter the amount to invest in WIPRO: "))

total_investment = tcs + coforge + hcltech + infy + ltm + lt + mphasis + persistent + techm + wipro
print("Total investment:", total_investment)

weitage_tcs = tcs / total_investment
weitage_coforge = coforge / total_investment
weitage_hcltech = hcltech / total_investment
weitage_infy = infy / total_investment
weitage_ltm = ltm / total_investment
weitage_lt = lt / total_investment
weitage_mphasis = mphasis / total_investment
weitage_persistent = persistent / total_investment
weitage_techm = techm / total_investment
weitage_wipro = wipro / total_investment
tatal_weightage = (weitage_tcs + weitage_coforge + weitage_hcltech + weitage_infy + weitage_ltm +
                    weitage_lt + weitage_mphasis + weitage_persistent + weitage_techm + weitage_wipro)
print("Total weightage:", tatal_weightage)

# ---- Day return calculation ----
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

portfolio_return = (return_tcs + return_coforge + return_hcltech + return_infy + return_ltm +
                     return_lt + return_mphasis + return_persistent + return_techm + return_wipro) / total_investment
print("Portfolio return:", portfolio_return)

# ---- 5 day return calculation ----
return_5day_tcs = df['TCS_5Day_Return'] * tcs
return_5day_coforge = df['COFORGE_5Day_Return'] * coforge
return_5day_hcltech = df['HCLTECH_5Day_Return'] * hcltech
return_5day_infy = df['INFY_5Day_Return'] * infy
return_5day_ltm = df['LTM_5Day_Return'] * ltm
return_5day_lt = df['LTTS_5Day_Return'] * lt
return_5day_mphasis = df['MPHASIS_5Day_Return'] * mphasis
return_5day_persistent = df['PERSISTENT_5Day_Return'] * persistent
return_5day_techm = df['TECHM_5Day_Return'] * techm
return_5day_wipro = df['WIPRO_5Day_Return'] * wipro

portfolio_5day_return = (return_5day_tcs + return_5day_coforge + return_5day_hcltech + return_5day_infy +
                          return_5day_ltm + return_5day_lt + return_5day_mphasis + return_5day_persistent +
                          return_5day_techm + return_5day_wipro) / total_investment
print("Portfolio Return for 5 day :", portfolio_5day_return)

# ---- 30 day return calculation ----
return_30day_tcs = df['TCS_30Day_Return'] * tcs
return_30day_coforge = df['COFORGE_30Day_Return'] * coforge
return_30day_hcltech = df['HCLTECH_30Day_Return'] * hcltech
return_30day_infy = df['INFY_30Day_Return'] * infy
return_30day_ltm = df['LTM_30Day_Return'] * ltm
return_30day_lt = df['LTTS_30Day_Return'] * lt
return_30day_mphasis = df['MPHASIS_30Day_Return'] * mphasis
return_30day_persistent = df['PERSISTENT_30Day_Return'] * persistent
return_30day_techm = df['TECHM_30Day_Return'] * techm
return_30day_wipro = df['WIPRO_30Day_Return'] * wipro

portfolio_30day_return = (return_30day_tcs + return_30day_coforge + return_30day_hcltech + return_30day_infy +
                           return_30day_ltm + return_30day_lt + return_30day_mphasis + return_30day_persistent +
                           return_30day_techm + return_30day_wipro) / total_investment
print("Portfolio Return for 30 days:", portfolio_30day_return)

# ---- 90 day return calculation ----
return_90day_tcs = df['TCS_90Day_Return'] * tcs
return_90day_coforge = df['COFORGE_90Day_Return'] * coforge
return_90day_hcltech = df['HCLTECH_90Day_Return'] * hcltech
return_90day_infy = df['INFY_90Day_Return'] * infy
return_90day_ltm = df['LTM_90Day_Return'] * ltm
return_90day_lt = df['LTTS_90Day_Return'] * lt
return_90day_mphasis = df['MPHASIS_90Day_Return'] * mphasis
return_90day_persistent = df['PERSISTENT_90Day_Return'] * persistent
return_90day_techm = df['TECHM_90Day_Return'] * techm
return_90day_wipro = df['WIPRO_90Day_Return'] * wipro

portfolio_90day_return = (return_90day_tcs + return_90day_coforge + return_90day_hcltech + return_90day_infy +
                           return_90day_ltm + return_90day_lt + return_90day_mphasis + return_90day_persistent +
                           return_90day_techm + return_90day_wipro) / total_investment
print("Portfolio Return for 90 days:", portfolio_90day_return)

# =========================================================================
# PORTFOLIO RETURN — END
# =========================================================================


# =========================================================================
# HISTORICAL VALUE AT RISK (VaR) — START
# =========================================================================

confidence_level = 0.95
historical_var = portfolio_return.quantile(1 - confidence_level)
print(f"Historical VaR for 1 day at {confidence_level*100}% confidence level: {historical_var*100}%")

confidence_level = 0.99
historical_var = portfolio_return.quantile(1 - confidence_level)
print(f"Historical VaR for 1 day at {confidence_level*100}% confidence level: {historical_var*100}%")

confidence_level = 0.95
historical_var = portfolio_5day_return.quantile(1 - confidence_level)
print(f"Historical VaR for 5 days at {confidence_level*100}% confidence level: {historical_var*100}%")

confidence_level = 0.99
historical_var = portfolio_5day_return.quantile(1 - confidence_level)
print(f"Historical VaR for 5 days at {confidence_level*100}% confidence level: {historical_var*100}%")

confidence_level = 0.95
historical_var = portfolio_30day_return.quantile(1 - confidence_level)
print(f"Historical VaR for 30 days at {confidence_level*100}% confidence level: {historical_var*100}%")

confidence_level = 0.99
historical_var = portfolio_30day_return.quantile(1 - confidence_level)
print(f"Historical VaR for 30 days at {confidence_level*100}% confidence level: {historical_var*100}%")

confidence_level = 0.95
historical_var = portfolio_90day_return.quantile(1 - confidence_level)
print(f"Historical VaR for 90 days at {confidence_level*100}% confidence level: {historical_var*100}%")

confidence_level = 0.99
historical_var = portfolio_90day_return.quantile(1 - confidence_level)
print(f"Historical VaR for 90 days at {confidence_level*100}% confidence level: {historical_var*100}%")

# =========================================================================
# HISTORICAL VALUE AT RISK (VaR) — END
# =========================================================================


# =========================================================================
# HISTORICAL CVaR (EXPECTED SHORTFALL) — START
# =========================================================================

confidence_level = 0.95
var_cutoff = portfolio_return.quantile(1 - confidence_level)
tail_returns = portfolio_return[portfolio_return <= var_cutoff]
cvar_1day_95 = tail_returns.mean()
print(f"Historical CVaR for 1 day at {confidence_level*100}% confidence level: {cvar_1day_95*100}%")

confidence_level = 0.99
var_cutoff = portfolio_return.quantile(1 - confidence_level)
tail_returns = portfolio_return[portfolio_return <= var_cutoff]
cvar_1day_99 = tail_returns.mean()
print(f"Historical CVaR for 1 day at {confidence_level*100}% confidence level: {cvar_1day_99*100}%")

confidence_level = 0.95
var_cutoff = portfolio_5day_return.quantile(1 - confidence_level)
tail_returns = portfolio_5day_return[portfolio_5day_return <= var_cutoff]
cvar_5day_95 = tail_returns.mean()
print(f"Historical CVaR for 5 days at {confidence_level*100}% confidence level: {cvar_5day_95*100}%")

confidence_level = 0.99
var_cutoff = portfolio_5day_return.quantile(1 - confidence_level)
tail_returns = portfolio_5day_return[portfolio_5day_return <= var_cutoff]
cvar_5day_99 = tail_returns.mean()
print(f"Historical CVaR for 5 days at {confidence_level*100}% confidence level: {cvar_5day_99*100}%")

confidence_level = 0.95
var_cutoff = portfolio_30day_return.quantile(1 - confidence_level)
tail_returns = portfolio_30day_return[portfolio_30day_return <= var_cutoff]
cvar_30day_95 = tail_returns.mean()
print(f"Historical CVaR for 30 days at {confidence_level*100}% confidence level: {cvar_30day_95*100}%")

confidence_level = 0.99
var_cutoff = portfolio_30day_return.quantile(1 - confidence_level)
tail_returns = portfolio_30day_return[portfolio_30day_return <= var_cutoff]
cvar_30day_99 = tail_returns.mean()
print(f"Historical CVaR for 30 days at {confidence_level*100}% confidence level: {cvar_30day_99*100}%")

confidence_level = 0.95
var_cutoff = portfolio_90day_return.quantile(1 - confidence_level)
tail_returns = portfolio_90day_return[portfolio_90day_return <= var_cutoff]
cvar_90day_95 = tail_returns.mean()
print(f"Historical CVaR for 90 days at {confidence_level*100}% confidence level: {cvar_90day_95*100}%")

confidence_level = 0.99
var_cutoff = portfolio_90day_return.quantile(1 - confidence_level)
tail_returns = portfolio_90day_return[portfolio_90day_return <= var_cutoff]
cvar_90day_99 = tail_returns.mean()
print(f"Historical CVaR for 90 days at {confidence_level*100}% confidence level: {cvar_90day_99*100}%")

# =========================================================================
# HISTORICAL CVaR (EXPECTED SHORTFALL) — END
# =========================================================================


# =========================================================================
# PORTFOLIO STATISTICS — START
# =========================================================================

portfolio_mean = portfolio_return.mean()
portfolio_variance = portfolio_return.var()
portfolio_std_dev = portfolio_return.std()
annualized_volatility = portfolio_std_dev * (252 ** 0.5)
print("Portfolio Mean (1-day):", portfolio_mean)
print("Portfolio Variance (1-day):", portfolio_variance)
print("Portfolio Standard Deviation (1-day):", portfolio_std_dev)
print("Annualized Volatility (from 1-day):", annualized_volatility)

portfolio_mean_5day = portfolio_5day_return.mean()
portfolio_variance_5day = portfolio_5day_return.var()
portfolio_std_dev_5day = portfolio_5day_return.std()
annualized_volatility_5day = portfolio_std_dev_5day * ((252 / 5) ** 0.5)
print("\nPortfolio Mean (5-day):", portfolio_mean_5day)
print("Portfolio Variance (5-day):", portfolio_variance_5day)
print("Portfolio Standard Deviation (5-day):", portfolio_std_dev_5day)
print("Annualized Volatility (from 5-day):", annualized_volatility_5day)

portfolio_mean_30day = portfolio_30day_return.mean()
portfolio_variance_30day = portfolio_30day_return.var()
portfolio_std_dev_30day = portfolio_30day_return.std()
annualized_volatility_30day = portfolio_std_dev_30day * ((252 / 30) ** 0.5)
print("\nPortfolio Mean (30-day):", portfolio_mean_30day)
print("Portfolio Variance (30-day):", portfolio_variance_30day)
print("Portfolio Standard Deviation (30-day):", portfolio_std_dev_30day)
print("Annualized Volatility (from 30-day):", annualized_volatility_30day)

portfolio_mean_90day = portfolio_90day_return.mean()
portfolio_variance_90day = portfolio_90day_return.var()
portfolio_std_dev_90day = portfolio_90day_return.std()
annualized_volatility_90day = portfolio_std_dev_90day * ((252 / 90) ** 0.5)
print("\nPortfolio Mean (90-day):", portfolio_mean_90day)
print("Portfolio Variance (90-day):", portfolio_variance_90day)
print("Portfolio Standard Deviation (90-day):", portfolio_std_dev_90day)
print("Annualized Volatility (from 90-day):", annualized_volatility_90day)

# =========================================================================
# PORTFOLIO STATISTICS — END
# =========================================================================


# =========================================================================
# PARAMETRIC VaR — START
# =========================================================================

z = 1.65
var_1 = (portfolio_mean - z * portfolio_std_dev) * total_investment
print("Parametric VaR for 1 DAY with 95% confidence is :", var_1)

z = 2.33
var_1_99 = (portfolio_mean - z * portfolio_std_dev) * total_investment
print("Parametric VaR for 1 DAY with 99% confidence is :", var_1_99)

z = 1.65
var_5 = (portfolio_mean_5day - z * portfolio_std_dev_5day) * total_investment
print("Parametric VaR for 5 DAY with 95% confidence is :", var_5)

z = 2.33
var_5_99 = (portfolio_mean_5day - z * portfolio_std_dev_5day) * total_investment
print("Parametric VaR for 5 DAY with 99% confidence is :", var_5_99)

z = 1.65
var_30 = (portfolio_mean_30day - z * portfolio_std_dev_30day) * total_investment
print("Parametric VaR for 30 DAY with 95% confidence is :", var_30)

z = 2.33
var_30_99 = (portfolio_mean_30day - z * portfolio_std_dev_30day) * total_investment
print("Parametric VaR for 30 DAY with 99% confidence is :", var_30_99)

z = 1.65
var_90 = (portfolio_mean_90day - z * portfolio_std_dev_90day) * total_investment
print("Parametric VaR for 90 DAY with 95% confidence is :", var_90)

z = 2.33
var_90_99 = (portfolio_mean_90day - z * portfolio_std_dev_90day) * total_investment
print("Parametric VaR for 90 DAY with 99% confidence is :", var_90_99)

# =========================================================================
# PARAMETRIC VaR — END
# =========================================================================


# =========================================================================
# PARAMETRIC EXPECTED SHORTFALL (ES) — START
# Formula: ES = mean - std_dev * [ e^(-z^2/2) / ((1 - confidence) * sqrt(2*pi)) ]
# Sign flipped to "-" (instead of "+") so ES comes out NEGATIVE like everything else
# =========================================================================

z = 1.65
confidence = 0.95
es_1_95 = (portfolio_mean - portfolio_std_dev * (math.exp(-(z ** 2) / 2) / ((1 - confidence) * math.sqrt(2 * math.pi)))) * total_investment
print("Parametric ES for 1 DAY with 95% confidence is :", es_1_95)

z = 2.33
confidence = 0.99
es_1_99 = (portfolio_mean - portfolio_std_dev * (math.exp(-(z ** 2) / 2) / ((1 - confidence) * math.sqrt(2 * math.pi)))) * total_investment
print("Parametric ES for 1 DAY with 99% confidence is :", es_1_99)

z = 1.65
confidence = 0.95
es_5_95 = (portfolio_mean_5day - portfolio_std_dev_5day * (math.exp(-(z ** 2) / 2) / ((1 - confidence) * math.sqrt(2 * math.pi)))) * total_investment
print("Parametric ES for 5 DAY with 95% confidence is :", es_5_95)

z = 2.33
confidence = 0.99
es_5_99 = (portfolio_mean_5day - portfolio_std_dev_5day * (math.exp(-(z ** 2) / 2) / ((1 - confidence) * math.sqrt(2 * math.pi)))) * total_investment
print("Parametric ES for 5 DAY with 99% confidence is :", es_5_99)

z = 1.65
confidence = 0.95
es_30_95 = (portfolio_mean_30day - portfolio_std_dev_30day * (math.exp(-(z ** 2) / 2) / ((1 - confidence) * math.sqrt(2 * math.pi)))) * total_investment
print("Parametric ES for 30 DAY with 95% confidence is :", es_30_95)

z = 2.33
confidence = 0.99
es_30_99 = (portfolio_mean_30day - portfolio_std_dev_30day * (math.exp(-(z ** 2) / 2) / ((1 - confidence) * math.sqrt(2 * math.pi)))) * total_investment
print("Parametric ES for 30 DAY with 99% confidence is :", es_30_99)

z = 1.65
confidence = 0.95
es_90_95 = (portfolio_mean_90day - portfolio_std_dev_90day * (math.exp(-(z ** 2) / 2) / ((1 - confidence) * math.sqrt(2 * math.pi)))) * total_investment
print("Parametric ES for 90 DAY with 95% confidence is :", es_90_95)

z = 2.33
confidence = 0.99
es_90_99 = (portfolio_mean_90day - portfolio_std_dev_90day * (math.exp(-(z ** 2) / 2) / ((1 - confidence) * math.sqrt(2 * math.pi)))) * total_investment
print("Parametric ES for 90 DAY with 99% confidence is :", es_90_99)

# =========================================================================
# PARAMETRIC EXPECTED SHORTFALL (ES) — END
# =========================================================================


# ==================================================================================================================
# BACKTESTING - START
# ==================================================================================================================


# =========================================================================
# BACKTESTING — STAGE 1: HISTORICAL VaR
# =========================================================================

# -------------------------------------------------------------------------
# 1 DAY — 95%
# -------------------------------------------------------------------------

historical_var_1day_95 = portfolio_return.quantile(0.05)
historical_breach_1day_95 = portfolio_return < historical_var_1day_95
historical_breaches_1day_95 = historical_breach_1day_95.sum()
total_observations_1day = portfolio_return.notna().sum()
historical_breach_rate_1day_95 = (historical_breaches_1day_95 / total_observations_1day)

print("\nHistorical VaR 1 DAY — 95%")
print("VaR:", historical_var_1day_95)
print("Number of breaches:", historical_breaches_1day_95)
print("Total observations:", total_observations_1day)
print("Actual breach rate:", historical_breach_rate_1day_95)
print("Expected breach rate:", 0.05)


# -------------------------------------------------------------------------
# 1 DAY — 99%
# -------------------------------------------------------------------------

historical_var_1day_99 = portfolio_return.quantile(0.01)
historical_breach_1day_99 = portfolio_return < historical_var_1day_99
historical_breaches_1day_99 = historical_breach_1day_99.sum()
historical_breach_rate_1day_99 = ( historical_breaches_1day_99 / total_observations_1day)

print("\nHistorical VaR 1 DAY — 99%")
print("VaR:", historical_var_1day_99)
print("Number of breaches:", historical_breaches_1day_99)
print("Total observations:", total_observations_1day)
print("Actual breach rate:", historical_breach_rate_1day_99)
print("Expected breach rate:", 0.01)


# -------------------------------------------------------------------------
# 5 DAYS — 95%
# -------------------------------------------------------------------------

historical_var_5day_95 = portfolio_5day_return.quantile(0.05)
historical_breach_5day_95 = portfolio_5day_return < historical_var_5day_95
historical_breaches_5day_95 = historical_breach_5day_95.sum()
total_observations_5day = portfolio_5day_return.notna().sum()
historical_breach_rate_5day_95 = (historical_breaches_5day_95 / total_observations_5day)

print("\nHistorical VaR 5 DAYS — 95%")
print("VaR:", historical_var_5day_95)
print("Number of breaches:", historical_breaches_5day_95)
print("Total observations:", total_observations_5day)
print("Actual breach rate:", historical_breach_rate_5day_95)
print("Expected breach rate:", 0.05)


# -------------------------------------------------------------------------
# 5 DAYS — 99%
# -------------------------------------------------------------------------

historical_var_5day_99 = portfolio_5day_return.quantile(0.01)
historical_breach_5day_99 = portfolio_5day_return < historical_var_5day_99
historical_breaches_5day_99 = historical_breach_5day_99.sum()
historical_breach_rate_5day_99 = (historical_breaches_5day_99 / total_observations_5day)

print("\nHistorical VaR 5 DAYS — 99%")
print("VaR:", historical_var_5day_99)
print("Number of breaches:", historical_breaches_5day_99)
print("Total observations:", total_observations_5day)
print("Actual breach rate:", historical_breach_rate_5day_99)
print("Expected breach rate:", 0.01)


# -------------------------------------------------------------------------
# 30 DAYS — 95%
# -------------------------------------------------------------------------

historical_var_30day_95 = portfolio_30day_return.quantile(0.05)
historical_breach_30day_95 = portfolio_30day_return < historical_var_30day_95
historical_breaches_30day_95 = historical_breach_30day_95.sum()
total_observations_30day = portfolio_30day_return.notna().sum()
historical_breach_rate_30day_95 = (historical_breaches_30day_95 / total_observations_30day)

print("\nHistorical VaR 30 DAYS — 95%")
print("VaR:", historical_var_30day_95)
print("Number of breaches:", historical_breaches_30day_95)
print("Total observations:", total_observations_30day)
print("Actual breach rate:", historical_breach_rate_30day_95)
print("Expected breach rate:", 0.05)


# -------------------------------------------------------------------------
# 30 DAYS — 99%
# -------------------------------------------------------------------------
historical_var_30day_99 = portfolio_30day_return.quantile(0.01)
historical_breach_30day_99 = portfolio_30day_return < historical_var_30day_99
historical_breaches_30day_99 = historical_breach_30day_99.sum()
historical_breach_rate_30day_99 = (historical_breaches_30day_99 / total_observations_30day)

print("\nHistorical VaR 30 DAYS — 99%")
print("VaR:", historical_var_30day_99)
print("Number of breaches:", historical_breaches_30day_99)
print("Total observations:", total_observations_30day)
print("Actual breach rate:", historical_breach_rate_30day_99)
print("Expected breach rate:", 0.01)


# -------------------------------------------------------------------------
# 90 DAYS — 95%
# -------------------------------------------------------------------------
historical_var_90day_95 = portfolio_90day_return.quantile(0.05)
historical_breach_90day_95 = portfolio_90day_return < historical_var_90day_95
historical_breaches_90day_95 = historical_breach_90day_95.sum()
total_observations_90day = portfolio_90day_return.notna().sum()
historical_breach_rate_90day_95 = (historical_breaches_90day_95 / total_observations_90day)

print("\nHistorical VaR 90 DAYS — 95%")
print("VaR:", historical_var_90day_95)
print("Number of breaches:", historical_breaches_90day_95)
print("Total observations:", total_observations_90day)
print("Actual breach rate:", historical_breach_rate_90day_95)
print("Expected breach rate:", 0.05)


# -------------------------------------------------------------------------
# 90 DAYS — 99%
# -------------------------------------------------------------------------

historical_var_90day_99 = portfolio_90day_return.quantile(0.01)
historical_breach_90day_99 = portfolio_90day_return < historical_var_90day_99
historical_breaches_90day_99 = historical_breach_90day_99.sum()
historical_breach_rate_90day_99 = (historical_breaches_90day_99 / total_observations_90day)

print("\nHistorical VaR 90 DAYS — 99%")
print("VaR:", historical_var_90day_99)
print("Number of breaches:", historical_breaches_90day_99)
print("Total observations:", total_observations_90day)
print("Actual breach rate:", historical_breach_rate_90day_99)
print("Expected breach rate:", 0.01)


# =========================================================================
# PARAMETRIC VaR BACKTESTING (FIXED — uses raw fraction VaR, not rupee-scaled)
# =========================================================================

z95 = 1.65
z99 = 2.33

# -------------------------------------------------------------------------
# 1 DAY — 95%
# -------------------------------------------------------------------------

param_var_1day_95 = portfolio_mean - z95 * portfolio_std_dev  # raw fraction, no total_investment
parametric_breach_1day_95 = portfolio_return < param_var_1day_95
parametric_breaches_1day_95 = parametric_breach_1day_95.sum()
parametric_breach_rate_1day_95 = (parametric_breaches_1day_95 / total_observations_1day)

print("\nParametric VaR 1 DAY — 95%")
print("VaR (fraction):", param_var_1day_95)
print("Number of breaches:", parametric_breaches_1day_95)
print("Total observations:", total_observations_1day)
print("Actual breach rate:", parametric_breach_rate_1day_95)
print("Expected breach rate:", 0.05)


# -------------------------------------------------------------------------
# 1 DAY — 99%
# -------------------------------------------------------------------------

param_var_1day_99 = portfolio_mean - z99 * portfolio_std_dev
parametric_breach_1day_99 = portfolio_return < param_var_1day_99
parametric_breaches_1day_99 = parametric_breach_1day_99.sum()
parametric_breach_rate_1day_99 = (parametric_breaches_1day_99 / total_observations_1day)

print("\nParametric VaR 1 DAY — 99%")
print("VaR (fraction):", param_var_1day_99)
print("Number of breaches:", parametric_breaches_1day_99)
print("Total observations:", total_observations_1day)
print("Actual breach rate:", parametric_breach_rate_1day_99)
print("Expected breach rate:", 0.01)


# -------------------------------------------------------------------------
# 5 DAYS — 95%
# -------------------------------------------------------------------------

param_var_5day_95 = portfolio_mean_5day - z95 * portfolio_std_dev_5day
parametric_breach_5day_95 = portfolio_5day_return < param_var_5day_95
parametric_breaches_5day_95 = parametric_breach_5day_95.sum()
parametric_breach_rate_5day_95 = (parametric_breaches_5day_95 / total_observations_5day)

print("\nParametric VaR 5 DAYS — 95%")
print("VaR (fraction):", param_var_5day_95)
print("Number of breaches:", parametric_breaches_5day_95)
print("Total observations:", total_observations_5day)
print("Actual breach rate:", parametric_breach_rate_5day_95)
print("Expected breach rate:", 0.05)


# -------------------------------------------------------------------------
# 5 DAYS — 99%
# -------------------------------------------------------------------------

param_var_5day_99 = portfolio_mean_5day - z99 * portfolio_std_dev_5day
parametric_breach_5day_99 = portfolio_5day_return < param_var_5day_99
parametric_breaches_5day_99 = parametric_breach_5day_99.sum()
parametric_breach_rate_5day_99 = (parametric_breaches_5day_99 / total_observations_5day)

print("\nParametric VaR 5 DAYS — 99%")
print("VaR (fraction):", param_var_5day_99)
print("Number of breaches:", parametric_breaches_5day_99)
print("Total observations:", total_observations_5day)
print("Actual breach rate:", parametric_breach_rate_5day_99)
print("Expected breach rate:", 0.01)


# -------------------------------------------------------------------------
# 30 DAYS — 95%
# -------------------------------------------------------------------------

param_var_30day_95 = portfolio_mean_30day - z95 * portfolio_std_dev_30day
parametric_breach_30day_95 = portfolio_30day_return < param_var_30day_95
parametric_breaches_30day_95 = parametric_breach_30day_95.sum()
parametric_breach_rate_30day_95 = (parametric_breaches_30day_95 / total_observations_30day)

print("\nParametric VaR 30 DAYS — 95%")
print("VaR (fraction):", param_var_30day_95)
print("Number of breaches:", parametric_breaches_30day_95)
print("Total observations:", total_observations_30day)
print("Actual breach rate:", parametric_breach_rate_30day_95)
print("Expected breach rate:", 0.05)


# -------------------------------------------------------------------------
# 30 DAYS — 99%
# -------------------------------------------------------------------------

param_var_30day_99 = portfolio_mean_30day - z99 * portfolio_std_dev_30day
parametric_breach_30day_99 = portfolio_30day_return < param_var_30day_99
parametric_breaches_30day_99 = parametric_breach_30day_99.sum()
parametric_breach_rate_30day_99 = (parametric_breaches_30day_99 / total_observations_30day)

print("\nParametric VaR 30 DAYS — 99%")
print("VaR (fraction):", param_var_30day_99)
print("Number of breaches:", parametric_breaches_30day_99)
print("Total observations:", total_observations_30day)
print("Actual breach rate:", parametric_breach_rate_30day_99)
print("Expected breach rate:", 0.01)


# -------------------------------------------------------------------------
# 90 DAYS — 95%
# -------------------------------------------------------------------------

param_var_90day_95 = portfolio_mean_90day - z95 * portfolio_std_dev_90day
parametric_breach_90day_95 = portfolio_90day_return < param_var_90day_95
parametric_breaches_90day_95 = parametric_breach_90day_95.sum()
parametric_breach_rate_90day_95 = (parametric_breaches_90day_95 / total_observations_90day)

print("\nParametric VaR 90 DAYS — 95%")
print("VaR (fraction):", param_var_90day_95)
print("Number of breaches:", parametric_breaches_90day_95)
print("Total observations:", total_observations_90day)
print("Actual breach rate:", parametric_breach_rate_90day_95)
print("Expected breach rate:", 0.05)


# -------------------------------------------------------------------------
# 90 DAYS — 99%
# -------------------------------------------------------------------------

param_var_90day_99 = portfolio_mean_90day - z99 * portfolio_std_dev_90day
parametric_breach_90day_99 = portfolio_90day_return < param_var_90day_99
parametric_breaches_90day_99 = parametric_breach_90day_99.sum()
parametric_breach_rate_90day_99 = (parametric_breaches_90day_99 / total_observations_90day)

print("\nParametric VaR 90 DAYS — 99%")
print("VaR (fraction):", param_var_90day_99)
print("Number of breaches:", parametric_breaches_90day_99)
print("Total observations:", total_observations_90day)
print("Actual breach rate:", parametric_breach_rate_90day_99)
print("Expected breach rate:", 0.01)

# =========================================================================
# PARAMETRIC VaR BACKTESTING — END
# =========================================================================

# =========================================================================
# STAGE 2 — KUPIEC TEST (PROPORTION OF FAILURES TEST)
# =========================================================================

# =========================================================================
# HISTORICAL VaR — 1 DAY — 95%
# =========================================================================

N = historical_breaches_1day_95
T = total_observations_1day
p = 0.05

p_hat = N / T

kupiec_lr_1day_95 = -2 * math.log(
    (
        ((1 - p) ** (T - N)) * (p ** N)
    )
    /
    (
        ((1 - p_hat) ** (T - N)) * (p_hat ** N)
    )
)

kupiec_pvalue_1day_95 = 1 - chi2.cdf(kupiec_lr_1day_95, 1)

print("\nKupiec Test — Historical VaR 1 DAY — 95%")
print("Number of breaches:", N)
print("Total observations:", T)
print("Expected breach probability:", p)
print("Observed breach probability:", p_hat)
print("Kupiec LR:", kupiec_lr_1day_95)
print("P-value:", kupiec_pvalue_1day_95)

if kupiec_pvalue_1day_95 > 0.05:
    print("Result: PASS — Fail to reject H0")
else:
    print("Result: FAIL — Reject H0")


# =========================================================================
# HISTORICAL VaR — 1 DAY — 99%
# =========================================================================

N = historical_breaches_1day_99
T = total_observations_1day
p = 0.01

p_hat = N / T

kupiec_lr_1day_99 = -2 * math.log(
    (
        ((1 - p) ** (T - N)) * (p ** N)
    )
    /
    (
        ((1 - p_hat) ** (T - N)) * (p_hat ** N)
    )
)

kupiec_pvalue_1day_99 = 1 - chi2.cdf(kupiec_lr_1day_99, 1)

print("\nKupiec Test — Historical VaR 1 DAY — 99%")
print("Number of breaches:", N)
print("Total observations:", T)
print("Expected breach probability:", p)
print("Observed breach probability:", p_hat)
print("Kupiec LR:", kupiec_lr_1day_99)
print("P-value:", kupiec_pvalue_1day_99)

if kupiec_pvalue_1day_99 > 0.05:
    print("Result: PASS — Fail to reject H0")
else:
    print("Result: FAIL — Reject H0")


# =========================================================================
# HISTORICAL VaR — 5 DAYS — 95%
# =========================================================================

N = historical_breaches_5day_95
T = total_observations_5day
p = 0.05

p_hat = N / T

kupiec_lr_5day_95 = -2 * math.log(
    (
        ((1 - p) ** (T - N)) * (p ** N)
    )
    /
    (
        ((1 - p_hat) ** (T - N)) * (p_hat ** N)
    )
)

kupiec_pvalue_5day_95 = 1 - chi2.cdf(kupiec_lr_5day_95, 1)

print("\nKupiec Test — Historical VaR 5 DAYS — 95%")
print("Number of breaches:", N)
print("Total observations:", T)
print("Expected breach probability:", p)
print("Observed breach probability:", p_hat)
print("Kupiec LR:", kupiec_lr_5day_95)
print("P-value:", kupiec_pvalue_5day_95)

if kupiec_pvalue_5day_95 > 0.05:
    print("Result: PASS — Fail to reject H0")
else:
    print("Result: FAIL — Reject H0")


# =========================================================================
# HISTORICAL VaR — 5 DAYS — 99%
# =========================================================================

N = historical_breaches_5day_99
T = total_observations_5day
p = 0.01

p_hat = N / T

kupiec_lr_5day_99 = -2 * math.log(
    (
        ((1 - p) ** (T - N)) * (p ** N)
    )
    /
    (
        ((1 - p_hat) ** (T - N)) * (p_hat ** N)
    )
)

kupiec_pvalue_5day_99 = 1 - chi2.cdf(kupiec_lr_5day_99, 1)

print("\nKupiec Test — Historical VaR 5 DAYS — 99%")
print("Number of breaches:", N)
print("Total observations:", T)
print("Expected breach probability:", p)
print("Observed breach probability:", p_hat)
print("Kupiec LR:", kupiec_lr_5day_99)
print("P-value:", kupiec_pvalue_5day_99)

if kupiec_pvalue_5day_99 > 0.05:
    print("Result: PASS — Fail to reject H0")
else:
    print("Result: FAIL — Reject H0")


# =========================================================================
# HISTORICAL VaR — 30 DAYS — 95%
# =========================================================================

N = historical_breaches_30day_95
T = total_observations_30day
p = 0.05

p_hat = N / T

kupiec_lr_30day_95 = -2 * math.log(
    (
        ((1 - p) ** (T - N)) * (p ** N)
    )
    /
    (
        ((1 - p_hat) ** (T - N)) * (p_hat ** N)
    )
)

kupiec_pvalue_30day_95 = 1 - chi2.cdf(kupiec_lr_30day_95, 1)

print("\nKupiec Test — Historical VaR 30 DAYS — 95%")
print("Number of breaches:", N)
print("Total observations:", T)
print("Expected breach probability:", p)
print("Observed breach probability:", p_hat)
print("Kupiec LR:", kupiec_lr_30day_95)
print("P-value:", kupiec_pvalue_30day_95)

if kupiec_pvalue_30day_95 > 0.05:
    print("Result: PASS — Fail to reject H0")
else:
    print("Result: FAIL — Reject H0")


# =========================================================================
# HISTORICAL VaR — 30 DAYS — 99%
# =========================================================================

N = historical_breaches_30day_99
T = total_observations_30day
p = 0.01

p_hat = N / T

kupiec_lr_30day_99 = -2 * math.log(
    (
        ((1 - p) ** (T - N)) * (p ** N)
    )
    /
    (
        ((1 - p_hat) ** (T - N)) * (p_hat ** N)
    )
)

kupiec_pvalue_30day_99 = 1 - chi2.cdf(kupiec_lr_30day_99, 1)

print("\nKupiec Test — Historical VaR 30 DAYS — 99%")
print("Number of breaches:", N)
print("Total observations:", T)
print("Expected breach probability:", p)
print("Observed breach probability:", p_hat)
print("Kupiec LR:", kupiec_lr_30day_99)
print("P-value:", kupiec_pvalue_30day_99)

if kupiec_pvalue_30day_99 > 0.05:
    print("Result: PASS — Fail to reject H0")
else:
    print("Result: FAIL — Reject H0")


# =========================================================================
# HISTORICAL VaR — 90 DAYS — 95%
# =========================================================================

N = historical_breaches_90day_95
T = total_observations_90day
p = 0.05

p_hat = N / T

kupiec_lr_90day_95 = -2 * math.log(
    (
        ((1 - p) ** (T - N)) * (p ** N)
    )
    /
    (
        ((1 - p_hat) ** (T - N)) * (p_hat ** N)
    )
)

kupiec_pvalue_90day_95 = 1 - chi2.cdf(kupiec_lr_90day_95, 1)

print("\nKupiec Test — Historical VaR 90 DAYS — 95%")
print("Number of breaches:", N)
print("Total observations:", T)
print("Expected breach probability:", p)
print("Observed breach probability:", p_hat)
print("Kupiec LR:", kupiec_lr_90day_95)
print("P-value:", kupiec_pvalue_90day_95)

if kupiec_pvalue_90day_95 > 0.05:
    print("Result: PASS — Fail to reject H0")
else:
    print("Result: FAIL — Reject H0")


# =========================================================================
# HISTORICAL VaR — 90 DAYS — 99%
# =========================================================================

N = historical_breaches_90day_99
T = total_observations_90day
p = 0.01

p_hat = N / T

kupiec_lr_90day_99 = -2 * math.log(
    (
        ((1 - p) ** (T - N)) * (p ** N)
    )
    /
    (
        ((1 - p_hat) ** (T - N)) * (p_hat ** N)
    )
)

kupiec_pvalue_90day_99 = 1 - chi2.cdf(kupiec_lr_90day_99, 1)

print("\nKupiec Test — Historical VaR 90 DAYS — 99%")
print("Number of breaches:", N)
print("Total observations:", T)
print("Expected breach probability:", p)
print("Observed breach probability:", p_hat)
print("Kupiec LR:", kupiec_lr_90day_99)
print("P-value:", kupiec_pvalue_90day_99)

if kupiec_pvalue_90day_99 > 0.05:
    print("Result: PASS — Fail to reject H0")
else:
    print("Result: FAIL — Reject H0")


# =========================================================================
# PARAMETRIC VaR — 1 DAY — 95%
# =========================================================================

N = parametric_breaches_1day_95
T = total_observations_1day
p = 0.05

p_hat = N / T

kupiec_lr_param_1day_95 = -2 * math.log(
    (
        ((1 - p) ** (T - N)) * (p ** N)
    )
    /
    (
        ((1 - p_hat) ** (T - N)) * (p_hat ** N)
    )
)

kupiec_pvalue_param_1day_95 = 1 - chi2.cdf(
    kupiec_lr_param_1day_95, 1
)

print("\nKupiec Test — Parametric VaR 1 DAY — 95%")
print("Number of breaches:", N)
print("Total observations:", T)
print("Expected breach probability:", p)
print("Observed breach probability:", p_hat)
print("Kupiec LR:", kupiec_lr_param_1day_95)
print("P-value:", kupiec_pvalue_param_1day_95)

if kupiec_pvalue_param_1day_95 > 0.05:
    print("Result: PASS — Fail to reject H0")
else:
    print("Result: FAIL — Reject H0")


# =========================================================================
# PARAMETRIC VaR — 1 DAY — 99%
# =========================================================================

N = parametric_breaches_1day_99
T = total_observations_1day
p = 0.01

p_hat = N / T

kupiec_lr_param_1day_99 = -2 * math.log(
    (
        ((1 - p) ** (T - N)) * (p ** N)
    )
    /
    (
        ((1 - p_hat) ** (T - N)) * (p_hat ** N)
    )
)

kupiec_pvalue_param_1day_99 = 1 - chi2.cdf(
    kupiec_lr_param_1day_99, 1
)

print("\nKupiec Test — Parametric VaR 1 DAY — 99%")
print("Number of breaches:", N)
print("Total observations:", T)
print("Expected breach probability:", p)
print("Observed breach probability:", p_hat)
print("Kupiec LR:", kupiec_lr_param_1day_99)
print("P-value:", kupiec_pvalue_param_1day_99)

if kupiec_pvalue_param_1day_99 > 0.05:
    print("Result: PASS — Fail to reject H0")
else:
    print("Result: FAIL — Reject H0")


# =========================================================================
# PARAMETRIC VaR — 5 DAYS — 95%
# =========================================================================

N = parametric_breaches_5day_95
T = total_observations_5day
p = 0.05

p_hat = N / T

kupiec_lr_param_5day_95 = -2 * math.log(
    (
        ((1 - p) ** (T - N)) * (p ** N)
    )
    /
    (
        ((1 - p_hat) ** (T - N)) * (p_hat ** N)
    )
)

kupiec_pvalue_param_5day_95 = 1 - chi2.cdf(
    kupiec_lr_param_5day_95, 1
)

print("\nKupiec Test — Parametric VaR 5 DAYS — 95%")
print("Number of breaches:", N)
print("Total observations:", T)
print("Expected breach probability:", p)
print("Observed breach probability:", p_hat)
print("Kupiec LR:", kupiec_lr_param_5day_95)
print("P-value:", kupiec_pvalue_param_5day_95)

if kupiec_pvalue_param_5day_95 > 0.05:
    print("Result: PASS — Fail to reject H0")
else:
    print("Result: FAIL — Reject H0")


# =========================================================================
# PARAMETRIC VaR — 5 DAYS — 99%
# =========================================================================

N = parametric_breaches_5day_99
T = total_observations_5day
p = 0.01

p_hat = N / T

kupiec_lr_param_5day_99 = -2 * math.log(
    (
        ((1 - p) ** (T - N)) * (p ** N)
    )
    /
    (
        ((1 - p_hat) ** (T - N)) * (p_hat ** N)
    )
)

kupiec_pvalue_param_5day_99 = 1 - chi2.cdf(
    kupiec_lr_param_5day_99, 1
)

print("\nKupiec Test — Parametric VaR 5 DAYS — 99%")
print("Number of breaches:", N)
print("Total observations:", T)
print("Expected breach probability:", p)
print("Observed breach probability:", p_hat)
print("Kupiec LR:", kupiec_lr_param_5day_99)
print("P-value:", kupiec_pvalue_param_5day_99)

if kupiec_pvalue_param_5day_99 > 0.05:
    print("Result: PASS — Fail to reject H0")
else:
    print("Result: FAIL — Reject H0")


# =========================================================================
# PARAMETRIC VaR — 30 DAYS — 95%
# =========================================================================

N = parametric_breaches_30day_95
T = total_observations_30day
p = 0.05

p_hat = N / T

kupiec_lr_param_30day_95 = -2 * math.log(
    (
        ((1 - p) ** (T - N)) * (p ** N)
    )
    /
    (
        ((1 - p_hat) ** (T - N)) * (p_hat ** N)
    )
)

kupiec_pvalue_param_30day_95 = 1 - chi2.cdf(
    kupiec_lr_param_30day_95, 1
)

print("\nKupiec Test — Parametric VaR 30 DAYS — 95%")
print("Number of breaches:", N)
print("Total observations:", T)
print("Expected breach probability:", p)
print("Observed breach probability:", p_hat)
print("Kupiec LR:", kupiec_lr_param_30day_95)
print("P-value:", kupiec_pvalue_param_30day_95)

if kupiec_pvalue_param_30day_95 > 0.05:
    print("Result: PASS — Fail to reject H0")
else:
    print("Result: FAIL — Reject H0")


# =========================================================================
# PARAMETRIC VaR — 30 DAYS — 99%
# =========================================================================

N = parametric_breaches_30day_99
T = total_observations_30day
p = 0.01

p_hat = N / T

kupiec_lr_param_30day_99 = -2 * math.log(
    (
        ((1 - p) ** (T - N)) * (p ** N)
    )
    /
    (
        ((1 - p_hat) ** (T - N)) * (p_hat ** N)
    )
)

kupiec_pvalue_param_30day_99 = 1 - chi2.cdf(
    kupiec_lr_param_30day_99, 1
)

print("\nKupiec Test — Parametric VaR 30 DAYS — 99%")
print("Number of breaches:", N)
print("Total observations:", T)
print("Expected breach probability:", p)
print("Observed breach probability:", p_hat)
print("Kupiec LR:", kupiec_lr_param_30day_99)
print("P-value:", kupiec_pvalue_param_30day_99)

if kupiec_pvalue_param_30day_99 > 0.05:
    print("Result: PASS — Fail to reject H0")
else:
    print("Result: FAIL — Reject H0")


# =========================================================================
# PARAMETRIC VaR — 90 DAYS — 95%
# =========================================================================

N = parametric_breaches_90day_95
T = total_observations_90day
p = 0.05

p_hat = N / T

kupiec_lr_param_90day_95 = -2 * math.log(
    (
        ((1 - p) ** (T - N)) * (p ** N)
    )
    /
    (
        ((1 - p_hat) ** (T - N)) * (p_hat ** N)
    )
)

kupiec_pvalue_param_90day_95 = 1 - chi2.cdf(
    kupiec_lr_param_90day_95, 1
)

print("\nKupiec Test — Parametric VaR 90 DAYS — 95%")
print("Number of breaches:", N)
print("Total observations:", T)
print("Expected breach probability:", p)
print("Observed breach probability:", p_hat)
print("Kupiec LR:", kupiec_lr_param_90day_95)
print("P-value:", kupiec_pvalue_param_90day_95)

if kupiec_pvalue_param_90day_95 > 0.05:
    print("Result: PASS — Fail to reject H0")
else:
    print("Result: FAIL — Reject H0")


# =========================================================================
# PARAMETRIC VaR — 90 DAYS — 99%
# =========================================================================

N = parametric_breaches_90day_99
T = total_observations_90day
p = 0.01

p_hat = N / T

kupiec_lr_param_90day_99 = -2 * math.log(
    (
        ((1 - p) ** (T - N)) * (p ** N)
    )
    /
    (
        ((1 - p_hat) ** (T - N)) * (p_hat ** N)
    )
)

kupiec_pvalue_param_90day_99 = 1 - chi2.cdf(
    kupiec_lr_param_90day_99, 1
)

print("\nKupiec Test — Parametric VaR 90 DAYS — 99%")
print("Number of breaches:", N)
print("Total observations:", T)
print("Expected breach probability:", p)
print("Observed breach probability:", p_hat)
print("Kupiec LR:", kupiec_lr_param_90day_99)
print("P-value:", kupiec_pvalue_param_90day_99)

if kupiec_pvalue_param_90day_99 > 0.05:
    print("Result: PASS — Fail to reject H0")
else:
    print("Result: FAIL — Reject H0")