import streamlit as st
import sys
from pathlib import Path

# Add your sections folder to path
dir = Path(__file__).absolute().parent
sys.path.append(str(dir / "sections"))

st.set_page_config(
    page_title="Aashay Zende Portfolio",
    page_icon="🎯",
    layout="wide"
)

# Inject CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

from utilities import render_about_information

render_about_information()

tabs = st.tabs([
    "Home",
    "Hobbies"
    "Project Boston",
    "E-Commerce Consulting Insights",
    
])

tab_home, tab_hobbies, tab_project_boston, tab_ecomm_consulting = tabs

with tab_home:
    from sections.home import run as run_home
    run_home()
    
with tab_hobbies:
    from sections.hobbies import run as run_hobbies
    run_hobbies()
    
with tab_project_boston:
    from sections.project_boston import run as run_project_boston
    run_project_boston()

with tab_ecomm_consulting:
    from sections.ecomm_consulting import run as run_ecomm_consulting
    run_ecomm_consulting()



st.divider()
st.markdown('[Back to Top](#aashay‑zende‑portfolio)')
