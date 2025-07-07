import streamlit as st
import base64
import sys
from pathlib import Path

# Add your sections folder to path
dir = Path(__file__).absolute().parent
sys.path.append(str(dir / "sections"))

# Page config
st.set_page_config(
    page_title="Aashay Zende Portfolio",
    page_icon="🎯",
    layout="wide"
)

# Inject CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# … (SVG/email renderer if needed, omit or adapt)

from utilities import render_about_information

render_about_information()
tabs = st.tabs([
    "Home",

    "Project Boston"
])

# Assign tab components
(
    tab_home,
    tab_after_hours,
    tab_carvana,
    tab_ecommerce,
    tab_powerbi,
    tab_project_boston,
    tab_random_widget,
    tab_tableau
) = tabs

with tab_home:
    from sections.home import run as run_home
    run_home()

with tab_after_hours:
    from sections.after_hours import run as run_after_hours
    run_after_hours()

with tab_carvana:
    from sections.carvana_case_study import run as run_carvana
    run_carvana()

with tab_ecommerce:
    from sections.ecommerce_insights import run as run_ecommerce
    run_ecommerce()

with tab_powerbi:
    from sections.powerbi import run as run_powerbi
    run_powerbi()

with tab_project_boston:
    from sections.project_boston import run as run_project_boston
    run_project_boston()

with tab_random_widget:
    from sections.random_widget_generator import run as run_random_widget
    run_random_widget()

with tab_tableau:
    from sections.tableau_dashboard import run as run_tableau
    run_tableau()

st.divider()
st.markdown('[Back to Top](#aashay‑zende‑portfolio)')
