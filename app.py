import streamlit as st


st.write("""
# Credit Card Approval Prediction App

This app predicts the credit card approval probablity
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    numerator = st.number_input("Numerator", min_value=-999999999.9999, max_value=999999999.9999)
    denominator = st.number_input("Denominator", min_value=-999999999.9999, max_value=999999999.9999)
    return numerator, denominator


Numerator, Denominator = user_input_features()
st.write(Numerator/Denominator)
