import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("Graph Plotting in Streamlit")

# Generate sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# --- 1. Using Matplotlib ---
st.subheader("Matplotlib Line Plot")
fig, ax = plt.subplots()
ax.plot(x, y, label='sin(x)')
ax.legend()
st.pyplot(fig)

# --- 2. Using Streamlit built-in line_chart ---
st.subheader("Streamlit Line Chart")
data = pd.DataFrame({'x': x, 'y': y})
st.line_chart(data.set_index('x'))
