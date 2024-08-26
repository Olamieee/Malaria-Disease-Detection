import streamlit as st
import numpy as np
import tensorflow as tf
import joblib
from tensorflow.keras.models import load_model
from PIL import Image
from sklearn.preprocessing import StandardScaler

# Load the trained model
model = joblib.load('mlp_malaria_model')
scaler = StandardScaler()
# Define a function for making predictions
def make_prediction(image):
    # Preprocess the image as required by the model
    image = image.resize((50, 50))
    image = np.array(image)
    image = scaler.fit_transform(image)  # standardize
    predict = model.predict(image)
    return predict

# Streamlit app
st.title("Image Classification with Streamlit")

st.write("Upload an image for classification:")

# File uploader for the image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    prediction = make_prediction(image)
    st.write(f"Prediction: {prediction}")
