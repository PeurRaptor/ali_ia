import pandas as pd
import numpy as np
import func

df=pd.read_csv("datasets/data.csv")
df=df.drop(columns=['Date'])
#df['differencehighclose']=df['High']-df['Close']
#df['differencelowclose']=df['Low']-df['Close']
end=len(df['prediction'])
beg=int(end*0.5)
#df['prediction'][beg:end]=func.linearregressionwithsplit(df.drop(columns=['prediction','Adj Close']),df['Close'],0.5)
#for i in range(2,11):
#        func.Polynomialregressionwithsplit(df.drop(columns=['prediction','Adj Close']),df['Close'],0.5,i)
df['prediction'][beg:end]=func.Polynomialregressionwithsplit(df.drop(columns=['prediction','Adj Close']),df['Close'],0.5,2)
print(df.describe())
print(df)