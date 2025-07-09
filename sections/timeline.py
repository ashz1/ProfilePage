# sections/timeline.py
import streamlit as st
from streamlit_timeline import timeline
import json

def run():
    st.markdown("### ✨ Career Timeline")

    timeline_data = {
        "title": {
            "media": {"url": ""},
            "text": {
                "headline": "Career Timeline",
                "text": "Professional and Academic Highlights"
            }
        },
        "events": [
        {
            "start_date": {"year": "2018", "month": "08"},
            "end_date": {"year": "2022", "month": "07"},
            "text": {"headline": "BTech - Automobile Engineering, MIT Manipal"}
        },
        {
            "start_date": {"year": "2019", "month": "03"},
            "end_date": {"year": "2021", "month": "05"},
            "text": {"headline": "Research Project - LoopMIT, Dept Head"}
        },
        {
            "start_date": {"year": "2021", "month": "05"},
            "end_date": {"year": "2021", "month": "07"},
            "text": {"headline": "R&D Intern - Mahindra & Mahindra"}
        },
        {
            "start_date": {"year": "2022", "month": "02"},
            "end_date": {"year": "2023", "month": "05"},
            "text": {"headline": "Business Analyst - Redseer Strategy"}
        },
        {
            "start_date": {"year": "2023", "month": "09"},
            "end_date": {"year": "2024", "month": "12"},
            "text": {"headline": "MS in Business Analytics - Northeastern University"}
        },
        {
            "start_date": {"year": "2025", "month": "01"},
            "text": {"headline": "Business Analyst - Radiant Consulting"}
        },
        {
            "start_date": {"year": "2024", "month": "04"},
            "text": {"headline": "Mentor & Teacher - TSNE / Dudley St Charter School"}
        },
        {
            "start_date": {"year": "2024", "month": "06"},
            "end_date": {"year": "2024", "month": "12"},
            "text": {"headline": "Business Analyst Intern - Clatch Fund"}
        }
        ]
    }

    timeline(json.dumps(timeline_data), height=600)
