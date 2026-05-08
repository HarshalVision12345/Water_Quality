import streamlit as st 
from PIL import Image
import requests
import numpy as np 
import pandas as pd 

water_img = Image.open(r"https://github.com/HarshalVision12345/Water_Quality/blob/master/Water_Quality/Gemini_Generated_Image_plw2juplw2juplw2.png")
st.image(water_img)

# USER INPUT FORM ---------------------> 
if st.button("About the water data"):
    st.write("1. ph: pH of 1. water (0 to 14)")
    st.write("2. Hardness: Capacity of water to precipitate soap in mg/L.")
    st.write("3. Solids: Total dissolved solids in ppm.")
    st.write("4. Chloramines: Amount of Chloramines in ppm.")
    st.write("5. Sulfate: Amount of Sulfates dissolved in mg/L")
    st.write("6. Conductivity: Electrical conductivity of water in μS/cm.")
    st.write("7. Organic_carbon: Amount of organic carbon in ppm.")
    st.write("8. Trihalomethanes: Amount of Trihalomethanes in μg/L.")
    st.write("9. Turbidity: Measure of light emiting property of water in NTU.")
    st.write("10. Potability: Indicates if water is safe for human consumption. Potable -1 and Not potable -0")

st.sidebar.header("Input Water Parameters")
Ph = st.sidebar.slider("PH",0.0,14.0,7.0)
Hardness = st.sidebar.slider("Hardness",47.432,323.124,196.3695)
Solids = st.sidebar.slider("Solids",320.94261,61227.196,22014.093)
Chloramines = st.sidebar.slider("Chloramines",0.352,13.127,7.1222768)
Sulfate = st.sidebar.slider("Sulfate",129.0,481.03064,333.77578)
Conductivity = st.sidebar.slider("Conductivity",181.48375,753.34262,426.20511)
Organic_carbon = st.sidebar.slider("Organic_carbon",2.2,28.3,14.28497)
Trihalomethanes = st.sidebar.slider("Trihalomethanes",0.738,124.0,66.396293)
Turbidity = st.sidebar.slider("Turbidity",1.45,6.739,3.966)

input_data = {
    "ph" : Ph,
    "Hardness" : Hardness,
    "Solids" : Solids,
    "Chloramines" : Chloramines,
    "Sulfate" : Sulfate,
    "Conductivity" : Conductivity,
    "Organic_carbon" : Organic_carbon,
    "Trihalomethanes" : Trihalomethanes,
    "Turbidity" : Turbidity

}

if st.button("Predict Water Potability"):
    try:
            
        response = requests.post("https://your-app-name.onrender.com/Predict", json=input_data)

        if response.status_code == 200 :
            result = response.json()
            prediction = result["Potability"]

        if prediction == 1 :
            st.success("✨ The water is Potable (Safe to drink)!")
        else : 
            st.error("⚠️ The water is Non-Potable (Not safe).")
    except Exception as e :
        st.error("⚠️ Connection Failed. Is your FastAPI server running?")
