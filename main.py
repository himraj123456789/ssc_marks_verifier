import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Generate some example data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot the data using Matplotlib
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Simple Plot')
plt.grid(True)

# Display the plot using Streamlit
st.pyplot(plt)
