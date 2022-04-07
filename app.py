import streamlit as st
import pandas as pd
import numpy as np

st.title("BMI Calculator")

# Ask for input
weight = st.number_input("Enter your Weight (lbs)", step=0.1)
height = st.number_input("Enter your Height (in)")

# bmi = weight/(height)**2
try:
    bmi = round(((weight * 703) / (height * height)), 2)
except ZeroDivisionError:
    st.warning("ZERO ERROR")

st.success(f"Your BMI is {bmi}")

#if bmi <= 18.5:
#    return "You are underweight."
#elif bmi <= 24.9:
#    return "You are healthy."
#elif bmi <= 29.8:
#    return "You are over weight."
#elif bmi <= 34.9:
#    return "You are severely over weight."
#elif bmi <= 39.9:
#    return "You are obese."
#else:
#    return "You are severely obese."
