@app.post("/predict")
def predict(data: dict):

    columns = [
        "District",
        "Commodity",
        "Min_Price",
        "Max_Price",
        "lag_1",
        "lag_7",
        "lag_30",
        "rolling_7",
        "rolling_30"
    ]

    df = pd.DataFrame([data])[columns]

    prediction = model.predict(df)[0]

    return {
        "predicted_price": float(prediction)
    }