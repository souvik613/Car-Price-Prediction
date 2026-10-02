import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("ford_model.pkl")

# Load dataset
df = pd.read_csv("ford.csv")

# Title
st.title("🚗 Car Price Prediction")

# Categorical inputs
model_name = st.selectbox(
    "Car Model",
    df["model"].unique()
)

transmission = st.selectbox(
    "Transmission",
    df["transmission"].unique()
)

fuelType = st.selectbox(
    "Fuel Type",
    df["fuelType"].unique()
)

# Numerical inputs
year = st.number_input(
    "Year",
    min_value=int(df["year"].min()),
    max_value=int(df["year"].max()),
    value=int(df["year"].max())
)

mileage = st.number_input(
    "Mileage",
    min_value=float(df["mileage"].min()),
    max_value=float(df["mileage"].max()),
    value=float(df["mileage"].mean())
)

tax = st.number_input(
    "Tax",
    min_value=float(df["tax"].min()),
    max_value=float(df["tax"].max()),
    value=float(df["tax"].mean())
)

mpg = st.number_input(
    "MPG",
    min_value=float(df["mpg"].min()),
    max_value=float(df["mpg"].max()),
    value=float(df["mpg"].mean())
)

engineSize = st.number_input(
    "Engine Size",
    min_value=float(df["engineSize"].min()),
    max_value=float(df["engineSize"].max()),
    value=float(df["engineSize"].mean())
)

# Prediction button
if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "model": [model_name],
        "year": [year],
        "transmission": [transmission],
        "mileage": [mileage],
        "fuelType": [fuelType],
        "tax": [tax],
        "mpg": [mpg],
        "engineSize": [engineSize]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted Car Price: £{prediction[0]:,.2f}")