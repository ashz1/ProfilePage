import streamlit as st
import base64

def run():
    st.title("Consulting Insights: Indian E-Commerce Market")
    st.divider()
    st.header("📄 Full Report (View Below)")

    # Path to your PDF file (must be in the same folder or accessible)
    pdf_file = "eComm India.pdf"

    # Display the PDF using an iframe
    with open(pdf_file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")

    pdf_display = f"""
    <iframe 
        src="data:application/pdf;base64,{base64_pdf}" 
        width="100%" 
        height="800px" 
        type="application/pdf">
    </iframe>
    """

    st.markdown(pdf_display, unsafe_allow_html=True)

    # Optional download button
    with open(pdf_file, "rb") as f:
        st.download_button(
            label="📥 Download PDF",
            data=f,
            file_name="eComm_India_Report.pdf",
            mime="application/pdf"
        )
