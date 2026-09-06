import pandas as pd
from functools import reduce

# =========================
# 1. CONFIG
# =========================

stocks = [
    "TCS.NS.C",
    "COFORGE.NS.C",
    "HCLTECH.NS.C",
    "INFY.NS.C",
    "LTM.NS.C",
    "LTTS.NS.C",
    "MPHASIS.NS.C",
    "PERSISTENT.NS.C",
    "TECHM.NS.C",
    "WIPRO.NS.C"
]

return_columns = [
    "Day_Return",
    "5Day_Return",
    "30Day_Return",
    "90Day_Return"
]

DATA_DIR = r"D:\IT QUANT\PROJECTS\var es project\data"


# =========================
# 2. LOAD EACH STOCK FILE
# =========================

dataframes = []

for stock in stocks:

    file_path = f"{DATA_DIR}\\{stock}.csv"

    temp_df = pd.read_csv(file_path)

    # Keep Date + required return columns
    temp_df = temp_df[
        ["Date"] + return_columns
    ].copy()

    # Temporary date only for matching
    temp_df["Date_Key"] = pd.to_datetime(
        temp_df["Date"],
        format="mixed",
        dayfirst=True
    )

    # Stock name
    clean_name = stock.split(".")[0]

    # Rename return columns
    rename_map = {
        col: f"{clean_name}_{col}"
        for col in return_columns
    }

    temp_df = temp_df.rename(
        columns=rename_map
    )

    dataframes.append(temp_df)


# =========================
# 3. COMBINE ALL FILES
# =========================

merged_frames = []

for i, temp_df in enumerate(dataframes):

    if i == 0:

        merged_frames.append(temp_df)

    else:

        # Remove original Date from other files
        merged_frames.append(
            temp_df.drop(columns=["Date"])
        )


portfolio_data = reduce(
    lambda left, right: pd.merge(
        left,
        right,
        on="Date_Key",
        how="outer"
    ),
    merged_frames
)


# =========================
# 4. SORT BY DATE
# =========================

portfolio_data = (
    portfolio_data
    .sort_values("Date_Key")
    .reset_index(drop=True)
)


# =========================
# 5. KEEP DATE FROM DATE_KEY
# =========================

portfolio_data["Date"] = portfolio_data["Date_Key"]


portfolio_data = portfolio_data.drop(
    columns=["Date_Key"]
)


# Put Date first
date_column = portfolio_data.pop("Date")

portfolio_data.insert(
    0,
    "Date",
    date_column
)


# =========================
# 6. CHECK
# =========================

print("\nMerged shape:")
print(portfolio_data.shape)

print("\nFirst 10 rows:")
print(portfolio_data.head(10))

print("\nMissing values:")
print(portfolio_data.isna().sum())

print("\nColumns:")
print(portfolio_data.columns.tolist())


# =========================
# 7. SAVE
# =========================

output_path = (
    f"{DATA_DIR}\\Portfolio_Returns_Merged.xlsx"
)

portfolio_data.to_excel(
    output_path,
    index=False
)

print(
    f"\nSaved successfully to:\n{output_path}"
)