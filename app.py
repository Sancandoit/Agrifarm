import streamlit as st

# Set page config
st.set_page_config(
    page_title="AgriFarm - Group 6 Dashboard",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <div style="background-color: rgba(255, 255, 255, 0.85); padding: 20px; border-radius: 10px;">
        <h1 style="color:#2e7d32;">🌱 AgriFarm - E-Business Strategy Dashboard</h1>
        <p>Interactive dashboard for Makro PRO / CP AXTRA case study</p>
        <ul>
            <li>📊 KPI Dashboard</li>
            <li>👩‍💼 Visionary Leaders</li>
            <li>👥 Team Group 6</li>
        </ul>
    </div>
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
