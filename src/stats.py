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

    #Descriptive Stats
    df['Mean'] = df["Day_Return"].mean()
    df['Median'] = df["Day_Return"].median()
    df['Std Dev'] = df["Day_Return"].std()
    df['Variance'] = df["Day_Return"].var()
    df['Skewness'] = df["Day_Return"].skew()
    df['Kurtosis'] = df["Day_Return"].kurt()    
    df['Min'] = df["Day_Return"].min()  
    df['Max'] = df["Day_Return"].max()

    # calculate volatility  
    df['Daily Volatility'] = df["Day_Return"].std()
    df['Annualized Volatility'] = df["Day_Return"].std() * (252 ** 0.5)
    df['Volatility 30'] = df["Day_Return"].rolling(window=30).std()
    df['Volatility 60'] = df["Day_Return"].rolling(window=60).std() 
    df['Volatility 90'] = df["Day_Return"].rolling(window=90).std()

    # save
    output_path = r"D:\IT QUANT\PROJECTS\var es project\data"
    df.to_csv(output_path + "\\" + stock + ".csv", index=False)