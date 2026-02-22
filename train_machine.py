import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

#sample machine data(replace with real data or db)
data=pd.DataFrame({"hours_used":[500,650,400,700],
                   "temperature":[32,35,28,38],
                   "failure":[0,1,0,1]})

X=data[["hours_used","temperature"]]
y=data["failure"]

model=RandomForestClassifier(n_estimators=100)
model.fit(X,y)

pickle.dump(model,open("machine_model.pkl","wb"))
print("Machine model trained successfully.")