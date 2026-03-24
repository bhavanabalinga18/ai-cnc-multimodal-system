import streamlit as st

st.set_page_config(page_title="AI CNC Dashboard", layout="wide")

st.title("🤖 AI CNC Multimodal System")
st.write("✅ App is running successfully")

try:
    # ALL your existing code here
    # (don’t delete anything, just keep inside try)

    import numpy as np
    import pandas as pd

    st.write("🚀 System initialized")

    # rest of your app code...

except Exception as e:
    st.error(f"Error: {e}")
