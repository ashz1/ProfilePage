import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

def run():
    col1, col2 = st.columns([2, 1.5])

    with col1:
        st.markdown("""
        #### I turn data into decisions. As a Business Analyst with a master’s in Business Analytics and a background in engineering, I’ve built end‑to‑end BI solutions that bridge strategy and technology, guiding global teams to clearer insights and smarter actions. Whether crafting interactive dashboards, designing automated data pipelines, or developing forecasting models with high accuracy, I focus on reliability and impact.

        My collaborative approach brings together finance, product, and development stakeholders to co‑create solutions that streamline processes and spotlight growth opportunities.

        Beyond consulting, I’m driven to lift up underserved youth through hands‑on teaching and mentoring. I teach game programming, 3D design & printing, and robotics at Dudley Street Charter School and Pathway Initiative – TSNE Boston.

        Off the clock, I’m usually behind a camera in nature, catching waves, kicking a soccer ball, or working on a canvas — see the hobbies section for more.
        """)

    with col2:
        st.image("6.jpg", use_container_width=True)

    # Display Resume PDF at the bottom
    st.markdown("### 📄 Resume")
    pdf_file_path = "Aashay R Zende - Resume.pdf"  # Ensure this path is correct
    pdf_viewer(pdf_file_path, width=700, height=1000)
