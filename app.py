import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import tensorflow as tf
from PIL import Image

# Load the saved model
MODEL_PATH = 'best_model.h5'  # Use a simpler path assuming the model is alongside app.py
try:
    model = load_model(MODEL_PATH)
except:
    st.error(f"Error loading model from {MODEL_PATH}. Make sure it's placed in the same directory as this file.")
    st.stop()


# Streamlit app
st.title("Deepfake Image Detector (ResNet18)")

st.write("""
Upload an image to classify it as **Real** or **Fake**.
""")


# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_column_width=True)
    
    # Preprocess the image
    img = img.resize((224, 224))

    img_array = np.array(img)
    if img_array.shape[-1] == 4:  # handle RGBA images
        img_array = img_array[:, :, :3]
        
    img_array = np.expand_dims(img_array, axis=0) / 255.0  # normalize


    # Predict
    prediction = model.predict(img_array)

    result = "Real" if prediction[0][0] < 0.5 else "Fake"
    confidence = (1 - prediction[0][0]) if result == "Real" else prediction[0][0]
    st.write(f"**Prediction:** {result} ({confidence * 100:.2f}% confidence)")
