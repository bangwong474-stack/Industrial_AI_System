import pandas as pd
#from sklearn.linear_model import LinearRegression
import pickle

df=pd.read_csv("production.csv")
print("Data loaded successfully")

X=df[["quantity","price"]]
y=df[["demand"]]

#model=LinearRegression()
#model.fit(X,y)

with open("production.pkl","wb")as file:
   # pickle.dump(model,file)

#print("Model saved successfully")