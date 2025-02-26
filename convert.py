import streamlit as st

# Function to convert meters to centimeters
def meter_to_cm(meters):
    return meters * 100

# Streamlit app layout
st.title("Meter to Centimeter Converter")

# User input for meters
meters = st.number_input("Enter value in meters:", min_value=0.0, step=0.1)

# Calculate the conversion when the user inputs a value
if meters is not None:
    cm = meter_to_cm(meters)
    st.write(f"{meters} meters is equal to {cm} centimeters.")
