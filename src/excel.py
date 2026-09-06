import pandas as pd

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

path = r"D:\IT QUANT\PROJECTS\var es project\data"
for stock in stocks:

    df = pd.read_csv(path + "\\" + stock + ".csv")

    # returns
    df['Day_Return'] = df["Adj Close"].pct_change(1)
    df['5Day_Return'] = df["Adj Close"].pct_change(5)
    df['10Day_Return'] = df["Adj Close"].pct_change(10)
    df['30Day_Return'] = df["Adj Close"].pct_change(30)
    df['60Day_Return'] = df["Adj Close"].pct_change(60)
    df['90Day_Return'] = df["Adj Close"].pct_change(90)
    df['180Day_Return'] = df["Adj Close"].pct_change(180)
    df['360Day_Return'] = df["Adj Close"].pct_change(360)

    # save
    output_path = r"D:\IT QUANT\PROJECTS\var es project\data"
    df.to_csv(output_path + "\\" + stock + ".csv", index=False)

    print(f"Processed {stock} and saved to {output_path}")