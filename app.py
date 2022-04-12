import streamlit as st
import pandas as pd
import numpy as np

st.title("BMI Calculator")

# Ask for input
weight = st.number_input("Enter your Weight (lbs)", step=1.0)
height = st.number_input("Enter your Height (in)", step=1.0)

# Catches 0 error and doesnt show message
try:
    bmi = round(((weight * 703) / (height * height)), 2)
    st.success(f"Your BMI is {bmi}")
except ZeroDivisionError:
    bmi = 0

# Show status under bmi calculation
if (bmi > 0):
    if bmi <= 18.5:
        st.success("You are underweight.")
    elif bmi <= 24.9:
        st.success("You are healthy.")
    elif bmi <= 29.8:
        st.success("You are over weight.")
    elif bmi <= 34.9:
        st.success("You are severely over weight.")
    elif bmi <= 39.9:
        st.success("You are obese.")
    else:
        st.success("You are severely obese.")
