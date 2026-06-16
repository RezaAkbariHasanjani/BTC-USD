import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def statistical(numeric_columns,df):
    minimum=[]
    maximum=[]
    mean_data=[]
    variance=[]
    standard_deviation=[]
    for i in numeric_columns:
        minimum.append(df[i].min())
        maximum.append(df[i].max()) 
        mean_data.append(df[i].mean())            
        variance.append(df[i].var())
        standard_deviation.append(df[i].std())
    return minimum, maximum, mean_data, variance,standard_deviation

df=pd.read_csv("BTC-USD.csv")
print(df)
df.info()
numeric_columns=["Close", "High", "Low", "Open", "Volume"]
df[numeric_columns]=df[numeric_columns].astype(np.float32)
df.info()
range_df=range(len(df))
Min, Max,mean_data, Var,Std=statistical(numeric_columns,df)
df_statistical=pd.DataFrame([Min,Max,mean_data,Var,Std])
df_statistical.index=['Min', 'Max', 'mean_data', 'Var', 'Std']
df_statistical.columns=["Close", "High", "Low", "Open", "Volume"]
print(df_statistical)
#-------------data plot----------------#
plt.figure(figsize=(16,12),dpi=100)
plt.subplot(2,3,1)
plt.plot(df['Date'],df['Close'], color='red')
plt.title("Data/Close")
plt.xlabel("Date")
plt.ylabel("Close")
plt.xticks(rotation=-90)
plt.legend(['Close'],loc='best')
plt.hlines(df_statistical.loc['mean_data','Close'], range_df[0],  range_df[-1], linestyle="dashed", label="mean_close")
plt.subplot(2,3,2)
plt.plot(df['Date'],df['High'], color='Blue')
plt.title("Data/High")
plt.xlabel("Date")
plt.ylabel("High")
plt.xticks(rotation=-90)
plt.legend(['High'],loc='best')
plt.hlines(df_statistical.loc['mean_data','High'], range_df[0],  range_df[-1], linestyle="dashed", label="mean_High")
plt.subplot(2,3,3)
plt.plot(df['Date'],df['Low'], color='green')
plt.title("Data/Low")
plt.xlabel("Date")
plt.ylabel("Low")
plt.xticks(rotation=-90)
plt.legend(['Low'],loc='best')
plt.hlines(df_statistical.loc['mean_data','Low'], range_df[0],  range_df[-1], linestyle="dashed", label="mean_Low")
plt.subplot(2,3,4)
plt.plot(df['Date'],df['Open'], color='black')
plt.title("Data/Low")
plt.xlabel("Date")
plt.ylabel("Open")
plt.xticks(rotation=-90)
plt.legend(['Open'],loc='best')
plt.hlines(df_statistical.loc['mean_data','Open'], range_df[0],  range_df[-1], linestyle="dashed", label="mean_Open")
plt.subplot(2,3,5)
plt.plot(df['Date'],df['Volume'], color='yellow')
plt.title("Data/Volume")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.xticks(rotation=-90)
plt.legend(['Volume'],loc='best')
plt.hlines(df_statistical.loc['mean_data','Volume'], range_df[0],  range_df[-1], linestyle="dashed", label="mean_Volume")
plt.savefig('BTC-USD', dpi=150)
plt.show()

