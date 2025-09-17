import streamlit as st

# Set page config
st.set_page_config(
    page_title="AgriFarm - Group 6 Dashboard",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
    <style>
        /* Make metric cards more stylish */
        [data-testid="stMetricValue"] {
            color: #2e7d32;  /* green */
            font-weight: bold;
        }
        [data-testid="stMetricLabel"] {
            font-size: 14px;
            font-weight: 500;
        }
    </style>
""", unsafe_allow_html=True)

# Main landing page
st.title("🌱 AgriFarm - E-Business Strategy Dashboard")
st.markdown("""
Welcome to the interactive dashboard for **Makro PRO / CP AXTRA** case study.  
Navigate through the pages on the sidebar to explore:
- 📊 KPI Dashboard  
- 👩‍💼 Visionary Leaders  
- 👥 Team Group 6
""")

# Footer
st.markdown("---")
st.caption("Created by Group 6: Sanchit Singh Thapa, Soniya Arunkumar, Chandraveer Singh, Pritish Dhal")
