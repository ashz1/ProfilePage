import os
from PIL import Image
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

def run():
    st.title("📄 Full Report – Indian E-Commerce Consulting Insights")
    st.write("Scroll through the pages below or download individual images or the full report as a PDF.")

    image_folder = "imgs"

    image_files = sorted(
        [f for f in os.listdir(image_folder) if f.endswith(".jpg")],
        key=lambda x: int(x.split(".")[0])
    )

    for img_file in image_files:
        img_path = os.path.join(image_folder, img_file)
        image = Image.open(img_path)
        st.image(image, use_container_width=True, caption=f"Page {img_file.split('.')[0]}")

    st.success("✅ End of Report")

    st.markdown("## 📘 View Full Report PDF")
    pdf_path = "Ecom_Report.pdf"
    if os.path.exists(pdf_path):
        pdf_viewer(pdf_path, width=1000)
        with open(pdf_path, "rb") as f:
            st.download_button(label="📥 Download Full PDF Report", data=f, file_name="Ecom_Report.pdf")
    else:
        st.warning("⚠️ Ecom_Report.pdf not found. Please check the file path.")

if __name__ == "__main__":
    run()
