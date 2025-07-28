import streamlit as st
import joblib
import numpy as np
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import urllib.request
import os

st.title("Draw & Predict with Pre-trained Model")

# Step 1: Download model if not already present
model_url = "https://github.com/himraj123456789/ssc_marks_verifier/raw/main/image_classifier.pkl"
model_path = "image_classifier.pkl"

if not os.path.exists(model_path):
    st.write("Downloading model...")
    urllib.request.urlretrieve(model_url, model_path)
    st.success("Model downloaded successfully!")

# Load model
model = joblib.load(model_path)

# Step 2: Create drawing canvas
st.subheader("Draw your image below:")
canvas_result = st_canvas(
    fill_color="black",       # Fill color for shapes
    stroke_width=8,           # Pen thickness
    stroke_color="white",     # Draw in white
    background_color="black", # Background in black
    width=256,
    height=256,
    drawing_mode="freedraw",
    key="canvas",
)

# Step 3: Process drawn image
if canvas_result.image_data is not None:
    img = Image.fromarray((canvas_result.image_data[:, :, 0]).astype('uint8'))  # Take red channel (grayscale)
    img = img.resize((64, 64))  # Resize to 64x64
    img_array = np.array(img)

    # Convert to binary (0 & 1)
    binary_img = (img_array > 127).astype(int)

    # Show processed binary image for debugging
    st.subheader("Processed Binary Image (what the model sees):")
    st.image(binary_img * 255, width=128)

    # Flatten input for model
    input_data = binary_img.flatten().reshape(1, -1)

    # Step 4: Predict button
    if st.button("Predict"):
        prediction = model.predict(input_data)
        st.success(f"Predicted Label: **{prediction[0]}**")
