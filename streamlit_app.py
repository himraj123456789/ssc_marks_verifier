import streamlit as st
import pdfplumber
import re
import pandas as pd
import io

from bs4 import BeautifulSoup
import requests
st.title("📄 UGC-NET PDF to DataFrame Converter + Text Echo")

# --- Step 1: File uploader ---
uploaded_file = st.file_uploader("Upload UGC-NET Answer Key PDF", type="pdf")

# --- Step 2: Simple text input ---
user_text = st.text_input("Enter any text you want (optional)")

# --- Step 3: Button to trigger extraction ---
if st.button("🔍 Extract Data and Show Text"):
    st.text_area("You Entered:", user_text)
    URL = user_text
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
    print(soup)
    if uploaded_file is not None:
        pdf_bytes = uploaded_file.read()
        extracted_data = []

        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
            total_pages = len(pdf.pages)
            st.info(f"Total Pages in PDF: {total_pages}")

            # --- Extract text from all pages ---
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    # Extract Question ID and Option (1–4)
                    page_data = re.findall(r'(\d{6,20})\s+([1-4])', text)
                    extracted_data.extend(page_data)

        # --- Show result in DataFrame ---
        if extracted_data:
            df = pd.DataFrame(extracted_data, columns=["Question ID", "Correct Option"])
            st.success(f"✅ Extracted {len(df)} rows.")
            st.dataframe(df)

            # Download option
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download as CSV", data=csv, file_name="ugc_net_answerkey.csv", mime='text/csv')
        else:
            st.warning("⚠️ No valid data found in the uploaded PDF.")
    else:
        st.warning("⚠️ Please upload a PDF file first.")
