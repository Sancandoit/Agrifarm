import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 KPI Dashboard - Makro PRO")

st.markdown("Use the sliders below to simulate adoption scenarios for Makro PRO.")

# Interactive controls
daily_orders = st.slider("Daily Orders", 1000, 10000, 5000, step=500)
skus = st.slider("SKUs Onboarded", 1000, 50000, 20000, step=1000)
adoption_rate = st.slider("Digital Adoption %", 10, 100, 60, step=5)
suppliers = st.slider("Suppliers Onboarded", 100, 10000, 2500, step=100)

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Daily Orders", f"{daily_orders:,}")
col2.metric("SKUs", f"{skus:,}")
col3.metric("Digital Adoption", f"{adoption_rate}%")
col4.metric("Suppliers", f"{suppliers:,}")

# Simulated GMV (simple model)
avg_order_value = 120  # assumption in USD
gmv = daily_orders * avg_order_value * 365
st.subheader("📈 Projected Annual GMV")
st.success(f"USD {gmv:,.0f}")

st.caption("These are simulated values for strategic exploration, not official data.")
