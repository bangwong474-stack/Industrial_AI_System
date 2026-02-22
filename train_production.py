import pandas as pd
import numpy as np
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

DATA_PATH="production.csv"

data=pd.read_csv(DATA_PATH)

le=LabelEncoder()
data["Products_encoded"]=le.fit_transform(data['product'])


X=data[['Products_encoded','product','price']]
y=data.loc[:,'demand']

#====train model=====
model=LinearRegression()
model.fit(X,y)

#=====save model====
with open("model.pkl","wb")as file:
    pickle.dump(model,file)

print("Data loaded successfully")
print(data.head())


if "month" in data.columns:
    data["month"]=pd.to_datetime(data["month"])
    data["month_Number"]=data["month"].dt.month


    FEATURES=["month_Number"]
    TARGET="production"

    X=data[FEATURES]
    y=data[TARGET]

    scaler=StandardScaler()
    X_scaled=scaler.fit_transform(X)

    X_train,X_test,y_train,y_test=train_test_split(X_scaled,y,test_size=0.2,random_state=42)

    model=LinearRegression()
    model.fit(X_train,y_train)

    print("Model trained successfully")


    y_pred=model.predict(X_test)

    mae=mean_absolute_error(y_test,y_pred)
    r2=r2_score(y_test,y_pred)

    print("\n=====MODEL EVALUATION=====")
    print(f"Mean Absolute Error:{mae:.2f}")
    print(f"R2 score:{r2:.2f}")


    MODEL_PATH="../models/production_model.pkl"
    SCALER_PATH="../models/production_scaler.pkl"

    os.makedirs("../models",exist_ok=True)

    pickle.dump(model,open(MODEL_PATH,"wb"))
    pickle.dump(scaler,open(SCALER_PATH,"wb"))

    print("\nModel Saved Successfully")
    print("Path:",MODEL_PATH)

    print("\nTraining proccess completed successfully")