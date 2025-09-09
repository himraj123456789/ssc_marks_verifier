import streamlit as st
import ascii_magic
from bs4 import BeautifulSoup
from PIL import Image
import tempfile
import os
import uuid
import streamlit.components.v1 as components

st.set_page_config(page_title="Custom ASCII Art Generator", layout="centered")

st.title("🎨 Image → Custom ASCII Art with Colors")
st.write("Upload an image, enter your custom text, and convert it into ASCII art (colors preserved).")

# Sidebar options
with st.sidebar:
    st.header("Options")
    columns = st.number_input("Columns (ASCII width)", min_value=10, max_value=1000, value=200, step=10)
    width_ratio = st.number_input("Width ratio (height scaling)", min_value=0.1, max_value=5.0, value=2.0, step=0.1)

# Input box for custom text
custom_text = st.text_area(
    "Enter the custom text to cycle through:",
    "",
    height=100
)

# File uploader
uploaded = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg", "bmp", "webp"])

if uploaded:
    img = Image.open(uploaded).convert("RGB")
    st.image(img, caption="Uploaded Image", use_column_width=True)

    if st.button("Generate ASCII Art"):
        if not custom_text.strip():
            st.error("Please enter some custom text before generating.")
        else:
            with st.spinner("Generating ASCII art..."):
                # Save uploaded image to a temp file
                tmp_in = os.path.join(tempfile.gettempdir(), f"{uuid.uuid4().hex}.png")
                img.save(tmp_in)

                # Output temp file for ascii_magic
                tmp_out = os.path.join(tempfile.gettempdir(), f"{uuid.uuid4().hex}_ascii.html")

                # Convert to ASCII HTML
                art = ascii_magic.AsciiArt.from_image(tmp_in)
                art.to_html_file(tmp_out, columns=columns, width_ratio=width_ratio)

                # Read HTML
                with open(tmp_out, "r", encoding="utf-8") as f:
                    html_content = f.read()

                # Replace characters with custom text (cycled)
                soup = BeautifulSoup(html_content, "html.parser")
                chars = list(custom_text)
                pr = 0
                for span in soup.find_all("span"):
                    if span.string:
                        span.string.replace_with(chars[pr])
                        pr = (pr + 1) % len(chars)

                final_html = str(soup)

                # Preview inside Streamlit
                components.html(final_html, height=600, scrolling=True)

                # Download button
                st.download_button(
                    label="Download index.html",
                    data=final_html.encode("utf-8"),
                    file_name="index.html",
                    mime="text/html"
                )

                st.success("✅ Done! Preview above and download with the button.")
