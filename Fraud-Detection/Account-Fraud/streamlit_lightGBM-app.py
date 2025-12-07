import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Fraud Detection App", layout="wide")

st.title("Fraud Detection Web App - LightGBM Model")

st.write("Upload transaction details to check if it's fraudulent.")

# Load model
model = joblib.load("fraud_detection_model_lightGBM.pkl")  # Replace with actual model path

# Input form
with st.form("fraud_form"):
    step = st.number_input("Step", min_value=0)
    t_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "CASH_IN", "DEBIT"], index=0)
    amount = st.number_input("Amount", min_value=0.0)
    oldbalanceOrg = st.number_input("Old Balance (Origin)", min_value=0.0)
    newbalanceOrig = st.number_input("New Balance (Origin)", min_value=0.0)
    oldbalanceDest = st.number_input("Old Balance (Destination)", min_value=0.0)
    newbalanceDest = st.number_input("New Balance (Destination)", min_value=0.0)

    submitted = st.form_submit_button("Predict Fraud")

if submitted:
    input_data = pd.DataFrame({
        "step": [step],
        "type": [t_type],
        "amount": [amount],
        "oldbalanceOrg": [oldbalanceOrg],
        "newbalanceOrig": [newbalanceOrig],
        "oldbalanceDest": [oldbalanceDest],
        "newbalanceDest": [newbalanceDest]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("This transaction is likely FRAUDULENT!")
    else:
        st.success("This transaction appears LEGITIMATE.")
st.write("Developed by Andrew En-maari Yahaya")