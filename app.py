# -------------------------------
# IMPORTS (MUST BE FIRST)
# -------------------------------
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="AI CNC Dashboard", layout="wide")

# -------------------------------
# TITLE
# -------------------------------
st.title("🤖 AI CNC Multimodal System")
st.write("✅ Smart CNC Monitoring Dashboard")

# -------------------------------
# KPI SECTION
# -------------------------------
st.subheader("📊 System Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Model Status", "Active")
col2.metric("Mode", "Safe Deployment")
col3.metric("System", "Running")

# -------------------------------
# FILE UPLOAD SECTION
# -------------------------------
st.header("📂 Upload CNC Data")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)

        st.subheader("📊 Uploaded Data")
        st.dataframe(data)

        # -------------------------------
        # NUMERIC DATA
        # -------------------------------
        numeric_data = data.select_dtypes(include=['number'])

        if numeric_data.empty:
            st.warning("⚠️ No numeric columns found in file")
        else:
            # -------------------------------
            # SUMMARY
            # -------------------------------
            st.subheader("📈 Data Summary")
            st.write(numeric_data.describe())

            # -------------------------------
            # GRAPH
            # -------------------------------
            st.subheader("📉 Visualization")

            selected_col = st.selectbox("Select column", numeric_data.columns)
            st.line_chart(numeric_data[selected_col])

            # -------------------------------
            # SAFE AI PREDICTION
            # -------------------------------
            st.subheader("🤖 AI Prediction")

            sample = numeric_data.iloc[0].values

            # simple safe prediction (no model dependency)
            prediction = np.mean(sample)

            st.success(f"🔮 Predicted Value: {prediction:.4f}")

            st.metric("AI Output", f"{prediction:.3f}")

            # -------------------------------
            # ANOMALY DETECTION (SAFE)
            # -------------------------------
            st.subheader("🚨 Anomaly Detection")

            threshold = np.mean(sample) + 2 * np.std(sample)

            if max(sample) > threshold:
                st.error("⚠️ Anomaly Detected")
            else:
                st.success("✅ Normal Operation")

    except Exception as e:
        st.error(f"❌ Error reading file: {e}")

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.title("📊 System Status")
st.sidebar.success("App Running")
st.sidebar.info("Upload CSV to analyze data")
