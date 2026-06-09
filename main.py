from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("apmc_price_model.pkl")

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

    return {
        "predicted_price": float(prediction)
    }