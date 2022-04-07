import streamlit as st
from PIL import Image

st.title("BMI Calculator")

# Ask for input
weight = st.number_input("Enter your Weight (lbs)", step=0.1)
height = st.number_input("Enter your Height (in)")

# bmi = weight/(height)**2
bmi = round(((weight * 703) / (height * height)), 2)

st.success(f"Your BMI is {bmi}")
