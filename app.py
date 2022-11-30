import streamlit as st


st.write("""
# Division of 2 numbers App

This app divides the first number buy the second number
""")

st.header('User Input Numbers')


def user_input_features():
    numerator = st.number_input("Numerator", min_value=-999999999.9999, max_value=999999999.9999)
    denominator = st.number_input("Denominator", min_value=-999999999.9999, max_value=999999999.9999)
    return numerator, denominator


Numerator, Denominator = user_input_features()
st.write("The value after division is:")
st.header(str(Numerator/Denominator))
