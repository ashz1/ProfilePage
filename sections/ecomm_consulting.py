import streamlit as st
from pdf2image import convert_from_path
from PIL import Image
import os

def run():
    st.title("Consulting Insights: Indian E-Commerce Market")
    st.divider()
    st.header("📄 Report Preview (Scroll to View Pages)")

    pdf_path = "eComm India.pdf"  # Make sure this is the correct filename

    try:
        # Convert PDF to a list of image objects
        images = convert_from_path(pdf_path, dpi=150)

        for i, image in enumerate(images):
            st.image(image, caption=f"Page {i + 1}", use_column_width=True)

        with open(pdf_path, "rb") as f:
            st.download_button(
                label="📥 Download Full Report (PDF)",
                data=f,
                file_name="eComm_India_Report.pdf",
                mime="application/pdf"
            )

    except Exception as e:
        st.error(f"Failed to load PDF: {e}")
