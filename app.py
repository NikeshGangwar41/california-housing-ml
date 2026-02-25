import streamlit as st
import pickle
import pandas as pd

# Page config
st.set_page_config(
    page_title="California Housing ML App",
    page_icon="🏡",
    layout="centered"
)

st.title("🏡 California Housing Price Predictor")
st.write("Random Forest Model")

# Load model
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

st.subheader("Enter House Details")

# Median Income in dollars
user_income = st.number_input(
    "Median Income ($)",
    min_value=10000,
    max_value=200000,
    value=60000,
    step=5000
)

# Convert to dataset scale
medinc = user_income / 10000

houseage = st.number_input("House Age", min_value=0.0, value=20.0, step=1.0)
averooms = st.number_input("Average Rooms", min_value=0.0, value=5.0, step=1.0)
avebedrms = st.number_input("Average Bedrooms", min_value=0.0, value=1.0, step=1.0)

# Input dataframe
input_data = pd.DataFrame({
    "MedInc": [medinc],
    "HouseAge": [houseage],
    "AveRooms": [averooms],
    "AveBedrms": [avebedrms]
})

st.subheader("Input Data (Model Scale)")
st.write(input_data)

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)[0]

    st.subheader("Results")
    st.success(f"🏠 Predicted House Price: ${prediction:,.0f}")