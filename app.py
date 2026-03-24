import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="AI CNC Dashboard", layout="wide")

st.title("🤖 AI CNC System")
st.write("🚀 Error-Free Smart Dashboard")

# Upload
st.header("📂 Upload CNC Data")
file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    try:
        df = pd.read_csv(file)

        st.subheader("📊 Data")
        st.dataframe(df)

        num_df = df.select_dtypes(include=['number'])

        if not num_df.empty:

            col = st.selectbox("Select column", num_df.columns)

            # SAFE GRAPH (NO EXTRA LIBRARY)
            st.line_chart(num_df[col])

            # Prediction
            val = np.mean(num_df.iloc[0])
            st.success(f"Prediction: {val:.3f}")

            # Future
            future = val * 1.1
            st.info(f"Future Prediction: {future:.3f}")

        else:
            st.warning("No numeric data found")

    except Exception as e:
        st.error(f"Error: {e}")
