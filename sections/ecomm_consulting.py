def run():
    import streamlit as st
    import os
    import shutil
    import numpy as np
    from PIL import Image
    from pdf2jpg import pdf2jpg

    st.title("Consulting Insights: Indian E-Commerce Market")
    st.markdown("""
    The Indian e-commerce market has demonstrated robust growth, innovation, and resilience. Here are the key insights and trends shaping the industry in 2022 and beyond.
    """)

    # ... [Your summary/insight sections here] ...

    st.divider()
    st.header("📄 Full Report (as Scrollable Image)")

    pdf_path = "eComm India.pdf"  # Ensure this matches your filename exactly

    def create_tmp_sub_folder():
        import tempfile
        tmp_dir = tempfile.mkdtemp()
        return tmp_dir

    def crop_white_space(img_arr):
        # Convert to grayscale if needed
        if img_arr.ndim == 3:
            gray = np.mean(img_arr, axis=2)
        else:
            gray = img_arr
        # Find all rows and columns that are not white (tolerance)
        mask = gray < 250
        coords = np.argwhere(mask)
        if coords.size == 0:
            return img_arr  # nothing to crop
        y0, x0 = coords.min(axis=0)
        y1, x1 = coords.max(axis=0) + 1  # slices are exclusive at the top
        return img_arr[y0:y1, x0:x1]

    def try_remove(path):
        try:
            shutil.rmtree(path)
        except Exception:
            pass

    display_method = "images"
    if display_method == "images":
        # Create temporary folder for generated image
        tmp_sub_folder_path = create_tmp_sub_folder()

        # Save images in that sub-folder
        result = pdf2jpg.convert_pdf2jpg(pdf_path, tmp_sub_folder_path, pages="ALL")
        images = []
        for image_path in result[0]["output_jpgfiles"]:
            images.append(np.array(Image.open(image_path)))

        # Create merged image from all images + remove irrelevant whitespace
        merged_arr = np.concatenate(images, axis=0)
        merged_arr = crop_white_space(merged_arr)
        merged_path = os.path.join(tmp_sub_folder_path, "merged.jpeg")
        Image.fromarray(merged_arr).save(merged_path, quality=95)

        # Display the image
        st.image(merged_path, use_column_width=True, caption="Full Report (scroll to view)")

        # Download button for the merged image
        with open(merged_path, "rb") as f:
            st.download_button(
                label="Download Full Report as Image (JPEG)",
                data=f,
                file_name="eComm_India_full_report.jpeg",
                mime="image/jpeg"
            )

        try_remove(tmp_sub_folder_path)

    st.info(
        "If the image does not display above, please use the download button. "
        "Large PDFs may take a few seconds to process."
    )
