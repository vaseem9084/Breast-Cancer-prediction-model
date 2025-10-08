import streamlit as st
import numpy as np
import pickle
import os

# Load the trained model safely
model_path = "model.pkl"

if os.path.exists(model_path):
    with open(model_path, "rb") as file:
        model = pickle.load(file)
else:
    st.error("❌ Model file 'model.pkl' not found. Please upload or place it in the same folder as app.py.")
    st.stop()
