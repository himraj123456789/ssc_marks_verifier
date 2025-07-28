import streamlit as st
import joblib
import cv2
import numpy as np
import urllib.request
import os

st.title("Image Classification using Pre-trained Model")

# Step 1: Download model if not already present
model_url = "https://github.com/himraj123456789/ssc_marks_verifier/raw/main/image_classifier.pkl"
model_path = "image_classifier.pkl"

if not os.path.exists(model_path):
    st.write("Downloading model...")
    urllib.request.urlretrieve(model_url, model_path)
    st.success("Model downloaded successfully!")

# Load the model
model = joblib.load(model_path)

# Step 2: Upload image
uploaded_file = st.file_uploader("Upload an image (64x64)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Read and display image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Step 3: Process Image (64x64 and binary)
    img = cv2.resize(img, (64, 64))  # Ensure correct size
    _, binary_img = cv2.threshold(img, 127, 1, cv2.THRESH_BINARY)
    input_data = binary_img.flatten().reshape(1, -1)

    # Step 4: Predict when button is pressed
    if st.button("Predict"):
        prediction = model.predict(input_data)
        st.success(f"Predicted Label: **{prediction[0]}**")
