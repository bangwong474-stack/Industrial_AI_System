import pickle

with open("production.pkl","rb")as file:
    model=pickle.load(file)

def predict(features):
    result=model.predict([features])
    return result

def machine_failure_rate(features):
    prediction=model.predict([features])
    machine_failure_rate=max(0,1-prediction[0]/100)
    return machine_failure_rate