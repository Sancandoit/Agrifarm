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
Welcome to the interactive dashboard for **Makro PRO / CP AXTRA**.

This interactive **Streamlit dashboard** was built as part of our MGB **E-Business Strategy course project** (Group 6).  
It showcases the CP AXTRA / Makro PRO case study, focusing on **go-to-market strategy, KPIs, and platform value creation**.  

---

## Navigate through the pages on the sidebar to explore:  
- **KPI Dashboard**: Simulate daily orders, SKU onboarding, adoption %, and supplier growth.  
- **Projected GMV Calculator**: Estimate annual gross merchandise value based on adoption scenarios.  
- **Visionary Leaders Page**: Profiles of Noppamas Sivakriskul & Simon Wintels, the McKinsey leaders who shaped the transformation.  
- **Team Group 6 Page**: Project credits and contributors. 
""")

# Footer
st.markdown("---")
st.caption("Created by Group 6: Sanchit Singh Thapa, Soniya Arunkumar, Chandraveer Singh, Pritish Dhal")
