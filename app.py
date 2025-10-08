import streamlit as st
import numpy as np
import pickle
import os

# Load the trained model
model = pickle.load(open("model.pkl", 'rb'))

# Set page configuration
st.set_page_config(page_title="Breast Cancer Prediction", layout="centered")

# ✅ Add only background color (like your HTML version)
st.markdown(
    """
    <style>
    /* Background color for the full app */
    [data-testid="stAppViewContainer"] {
        background-color: Bisque;
        color: black;
    }

    /* Input label styling */
    .stTextInput label {
        font-weight: bold;
        color: black;
    }

    h1, h2, h3 {
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Check if image exists before displaying
image_path = "combine.png"
if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)
else:
    st.warning("⚠️ 'combine.png' not found. Please place it in the same folder as this app.py file.")

# Title
st.title("Breast Cancer Prediction Model")

# User Input
st.subheader("Input All Breast Cancer Features")
features = st.text_input(
    "Enter features separated by commas (e.g., 17.99,10.38,122.8,1001,0.1184,...)"
)

# Predict Button
if st.button("Submit"):
    try:
        # Convert input text to numpy array
        features_list = features.split(',')
        np_features = np.asarray(features_list, dtype=np.float32).reshape(1, -1)

        # Make prediction
        pred = model.predict(np_features)

        # Display Results
        if pred[0] == 1:
            cancer_img = "Breast_Cancer1.png"
            if os.path.exists(cancer_img):
                st.image(cancer_img, width=300)
            else:
                st.warning("Cancer image not found — please add 'Breast_Cancer1.png' in your folder.")

            st.subheader("🩸 Cancerous")
            st.write("""
            Breast cancer occurs when cells in the breast grow abnormally and multiply uncontrollably,
            forming a lump or mass. Early detection through regular screening and treatment greatly 
            improves recovery chances.
            """)
        else:
            not_cancer_img = "not cancer image.jpg"
            if os.path.exists(not_cancer_img):
                st.image(not_cancer_img, width=300)
            else:
                st.warning("Normal image not found — please add 'not cancer image.jpg' in your folder.")

            st.subheader("✅ Not Cancerous")
            st.write("""
            A normal breast without cancer contains healthy tissue with milk glands, ducts, and connective tissue.
            The cells grow in an orderly way, with no abnormal lumps or uncontrolled growth.
            """)

    except Exception as e:
        st.error(f"Error: {e}")
