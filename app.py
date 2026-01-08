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
st.write("Linear Regression & Logistic Regression Models")

# Load models
@st.cache_resource
def load_models():
    with open("linear_regression_model.pkl", "rb") as f:
        linear_model = pickle.load(f)
    with open("logistic_regression_model.pkl", "rb") as f:
        logistic_model = pickle.load(f)
    return linear_model, logistic_model

linear_model, logistic_model = load_models()

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

houseage = st.number_input("House Age", min_value=0.0, value=20.0,step=1.0)
averooms = st.number_input("Average Rooms", min_value=0.0, value=5.0,step=1.0)
avebedrms = st.number_input("Average Bedrooms", min_value=0.0, value=1.0,step=1.0)

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
    price_pred = linear_model.predict(input_data)[0]
    class_pred = logistic_model.predict(input_data)[0]
    prob_pred = logistic_model.predict_proba(input_data)[0][1]

    st.subheader("Results")
    st.success(f"🏠 Predicted House Price: ${price_pred:,.0f}")

    if class_pred == 1:
        st.info(f"📈 Price Category: HIGH ({prob_pred:.2%} confidence)")
    else:
        st.info(f"📉 Price Category: LOW ({1 - prob_pred:.2%} confidence)")
