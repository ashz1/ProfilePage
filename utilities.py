import streamlit as st

def render_about_information():
    st.markdown(
        """
        <h1 style='text-align: center;'>Aashay Zende</h1>
        <h3 style='text-align: center;'>Business Analyst | Data Engineer | Educator</h3>
        <h6 style='text-align: center;'>  <a href="mailto:aashayzende@gmail.com">aashayzende@gmail.com</a> • +1 857‑397‑2290 • Boston, MA </h6>
        """,
        unsafe_allow_html=True
    )

    st.subheader("[aashayzende@gmail.com](mailto:aashayzende@gmail.com) • +1 857‑397‑2290 • Boston, MA", divider=True)
