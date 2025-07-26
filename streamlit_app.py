import streamlit as st
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from PIL import Image

csv_url = "https://raw.githubusercontent.com/himraj123456789/saurav/main/hhh.csv"

st.title("PCA Image Reconstruction")

df = pd.read_csv(csv_url, header=None)
loaded_array = df.to_numpy()

st.write(f"Original data shape: {loaded_array.shape}")

n_components = st.number_input(
    "Enter number of PCA components", min_value=1, max_value=min(loaded_array.shape), value=30, step=1
)

if st.button("Apply PCA"):
    pca = PCA(n_components=n_components)
    transformed = pca.fit_transform(loaded_array)
    reconstructed = pca.inverse_transform(transformed)

    # Normalize arrays for display (0-255)
    def to_image(arr):
        arr = arr - arr.min()
        arr = arr / arr.max()
        arr = (arr * 255).astype(np.uint8)
        return Image.fromarray(arr)

    original_img = to_image(loaded_array)
    reconstructed_img = to_image(reconstructed)

    st.image([original_img, reconstructed_img], caption=["Original", f"Reconstructed ({n_components})"])
