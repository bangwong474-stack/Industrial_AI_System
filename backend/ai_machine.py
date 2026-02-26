import joblib

model=joblib.load("production.pkl")

def predict(data):
   prediction=model.predict([data])
   return prediction.tolist()

def machine_failure_rate(features):
    prediction=model.predict([features])
    machine_failure_rate=max(0,1-prediction[0]/100)
    return machine_failure_rate