import pandas as pd


# --------------------------------------------------
# 1. Stock list
# --------------------------------------------------

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


# --------------------------------------------------
# 2. Folder path
# --------------------------------------------------

path = r"D:\IT QUANT\PROJECTS\var es project\data"


# --------------------------------------------------
# 3. Create empty combined DataFrame
# --------------------------------------------------

combined = pd.DataFrame()


# --------------------------------------------------
# 4. Read all stock files
# --------------------------------------------------

for stock in stocks:

    print("Reading:", stock)

    df = pd.read_csv(path + "\\" + stock + ".csv")

    # Keep only Date and Day_Return
    stock_data = df[["Date", "Day_Return"]].copy()

    # Convert Date only for matching
    stock_data["Date_Check"] = pd.to_datetime(
    stock_data["Date"],
    format="mixed",
    dayfirst=True
)
    

    # Keep only the date used for matching
    # and the return
    stock_data = stock_data[["Date_Check", "Day_Return"]]

    # Rename Day_Return to stock name
    stock_data = stock_data.rename(
        columns={
            "Day_Return": stock
        }
    )


    # --------------------------------------------------
    # 5. Combine stocks using common dates
    # --------------------------------------------------

    if combined.empty:

        combined = stock_data

    else:

        combined = pd.merge(
            combined,
            stock_data,
            on="Date_Check",
            how="inner"
        )


# --------------------------------------------------
# 6. Rename Date_Check back to Date
# --------------------------------------------------

combined = combined.rename(
    columns={
        "Date_Check": "Date"
    }
)


# --------------------------------------------------
# 7. Sort by date
# --------------------------------------------------

combined = combined.sort_values("Date")


# --------------------------------------------------
# 8. Reset row numbers
# --------------------------------------------------

combined = combined.reset_index(drop=True)


# --------------------------------------------------
# 9. Save combined file
# --------------------------------------------------

combined.to_csv(
    path + "\\combined_returns.csv",
    index=False
)


# --------------------------------------------------
# 10. Display results
# --------------------------------------------------

print("\n--------------------------------------")
print("COMBINED DATASET CREATED")
print("--------------------------------------")

print("Rows:", len(combined))
print("Columns:", len(combined.columns))

print("\nFirst 5 rows:")
print(combined.head())

print("\nLast 5 rows:")
print(combined.tail())

print("\nFile saved as:")
print(path + "\\combined_returns.csv")