import streamlit as st
import joblib

# load trained model
model = joblib.load("model.pkl")

st.title("Subscription Renewal Prediction App")

st.write("Enter customer details to predict renewal")

# Inputs (must match training features EXACTLY)
age = st.number_input("Age")
tenure = st.number_input("Tenure")
monthly_charges = st.number_input("Monthly Charges")
total_charges = st.number_input("Total Charges")

# Prediction
if st.button("Predict"):

    input_data = [[age, tenure, monthly_charges, total_charges]]

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Customer will renew subscription")
    else:
        st.error("Customer will not renew subscription")
