from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import numpy as np 
import pandas as pd 

app = FastAPI(title="Water Quality Predictor API")

model = joblib.load("water_model.pkl")

class Water_features(BaseModel):
    ph : float  
    Hardness : float
    Solids : float
    Chloramines : float
    Sulfate : float
    Conductivity : float
    Organic_carbon : float
    Trihalomethanes : float
    Turbidity : float

@app.post("/Predict")
def Predict_quality(data:Water_features):
    data_dict = data.dict()

    input_df = pd.DataFrame([data_dict])

    prediction = model.predict(input_df)
    return {f"Potability" : int(prediction[0])}