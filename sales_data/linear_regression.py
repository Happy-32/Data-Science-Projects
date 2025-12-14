import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("Linear-Regression.pkl")

st.set_page_config(page_title="Revenue Prediction App", layout="centered")

st.title("💰 Revenue Prediction App")
st.write("Predict expected revenue based on order characteristics")

# -----------------------
# User Inputs
# -----------------------
product = st.selectbox("Product", [
    "Burgers", "Fries", "Chicken Sandwiches", 'Beverages', 'Sides & Other'
])

city = st.selectbox("City", [
    "Lisbon", "London", "Madrid", "Paris", 'Berlin'
])

manager = st.selectbox("Manager", [
    "Tom Jackson", "Pablo Perez", "Joao Silva", "Remy Monet", "Walter Muller"
])

purchase_type = st.selectbox("Purchase Type", [
    "Online", "In-Store", "Drive-Thru"
])

payment_method = st.selectbox("Payment Method", [
    "Credit Card", "Cash", "Gift Card"
])

# -----------------------
# Create input DataFrame
# -----------------------
input_df = pd.DataFrame({
    "Product": [product],
    "City": [city],
    "Manager": [manager],
    "Purchase Type": [purchase_type],
    "Payment Method": [payment_method]
})

# -----------------------
# Prediction
# -----------------------
if st.button("Predict Revenue"):
    prediction = model.predict(input_df)[0]
    st.success(f"💵 Predicted Revenue: ${prediction:,.2f}")
    st.balloons()