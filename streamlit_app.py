import streamlit as st
import joblib
from PIL import Image
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
    # Open image using PIL
    img = Image.open(uploaded_file).convert("L")  # Convert to grayscale
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Step 3: Resize and convert to binary (0/1)
    img = img.resize((64, 64))
    img_array = np.array(img)

    # Convert grayscale to binary (threshold at 127)
    binary_img = (img_array > 127).astype(int)

    # Flatten the binary image into 4096 features
    input_data = binary_img.flatten().reshape(1, -1)

    # Step 4: Predict when button is pressed
    if st.button("Predict"):
        prediction = model.predict(input_data)
        st.success(f"Predicted Label: **{prediction[0]}**")
