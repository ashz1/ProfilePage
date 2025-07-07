import os
from PIL import Image
import streamlit as st
def run():
    st.title("📄 Full Report – Indian E-Commerce Consulting Insights")
    st.write("Scroll through the pages below or download individual images as needed.")

    image_folder = "imgs"
    
    # Collect and sort images by numeric order
    image_files = sorted(
        [f for f in os.listdir(image_folder) if f.endswith(".jpg")],
        key=lambda x: int(x.split(".")[0])
    )

    # Display all images
    for img_file in image_files:
        img_path = os.path.join(image_folder, img_file)
        image = Image.open(img_path)
        st.image(image, use_column_width=True, caption=f"Page {img_file.split('.')[0]}")

    st.success("✅ End of Report")

if __name__ == "__main__":
    run()
