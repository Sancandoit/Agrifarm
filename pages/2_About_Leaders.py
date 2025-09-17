import streamlit as st

st.title("👩‍💼 Visionary Leaders Behind Makro PRO")

col1, col2 = st.columns(2)

with col1:
    st.image("assets/noppamas", width=250)
    st.subheader("Noppamas Sivakriskul")
    st.write("**Senior Partner and Managing Partner, Bangkok**")
    st.caption("Leads McKinsey’s digital business-building work in Southeast Asia and advises B2B and B2C companies across the continent.")

with col2:
    st.image("assets/simon", width=250)
    st.subheader("Simon Wintels")
    st.write("**Partner, Amsterdam**")
    st.caption("Helps consumer-goods and retail clients capture growth through excellence in strategy, digital and advanced analytics, and marketing.")
