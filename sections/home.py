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
    
    pdf_file_path = "Aashay R Zende - Resume.pdf"  # Ensure this path is correct
    pdf_viewer(pdf_file_path, width=700, height=1000)
    with open(pdf_file_path, "rb") as f:
        st.download_button(
            label="Download Resume",
            data=f,
            file_name="Aashay_R_Zende_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    # Timeline
    st.markdown("### 📅 Timeline")
    timeline_data = {
        "title": {"media": {"url": ""}, "text": {"headline": "Career Timeline", "text": "Professional and Academic Highlights"}},
        "events": [
            {"start_date": {"year": "2018", "month": "08"}, "text": {"headline": "BTech - Automobile Engineering, MIT Manipal"}},
            {"start_date": {"year": "2019", "month": "03"}, "text": {"headline": "Research Project - LoopMIT, Dept Head"}},
            {"start_date": {"year": "2021", "month": "05"}, "end_date": {"year": "2021", "month": "07"}, "text": {"headline": "Mahindra & Mahindra, R&D Intern"}},
            {"start_date": {"year": "2022", "month": "02"}, "end_date": {"year": "2023", "month": "05"}, "text": {"headline": "Business Analyst - Redseer Strategy"}},
            {"start_date": {"year": "2023", "month": "09"}, "text": {"headline": "MS in Business Analytics - Northeastern"}},
            {"start_date": {"year": "2024", "month": "01"}, "text": {"headline": "Business Analyst - Radiant Consulting"}},
            {"start_date": {"year": "2024", "month": "04"}, "text": {"headline": "Mentor & Teacher - TSNE Pathway / Dudley Charter"}},
            {"start_date": {"year": "2024", "month": "06"}, "end_date": {"year": "2024", "month": "12"}, "text": {"headline": "Business Analyst Intern - Clatch Fund"}},
        ]
    }

    timeline(json.dumps(timeline_data), height=600)
