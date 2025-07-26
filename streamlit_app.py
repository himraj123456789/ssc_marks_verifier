import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# GitHub CSV URL
csv_url = "https://raw.githubusercontent.com/himraj123456789/saurav/main/hhh.csv"

st.title("PCA Image Reconstruction")

# Load CSV into DataFrame (assuming no header)
df = pd.read_csv(csv_url, header=None)
loaded_array = df.to_numpy()

st.write(f"Original data shape: {loaded_array.shape}")

# Input PCA components
n_components = st.number_input(
    "Enter number of PCA components", min_value=1, max_value=min(loaded_array.shape), value=30, step=1
)

if st.button("Apply PCA"):
    # Apply PCA
    pca = PCA(n_components=n_components)
    transformed = pca.fit_transform(loaded_array)
    reconstructed = pca.inverse_transform(transformed)

    # Plotting
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    axs[0].imshow(loaded_array, cmap='gray')
    axs[0].set_title("Original")
    axs[0].axis('off')

    axs[1].imshow(reconstructed, cmap='gray')
    axs[1].set_title(f"Reconstructed with {n_components} components")
    axs[1].axis('off')

    st.pyplot(fig)
