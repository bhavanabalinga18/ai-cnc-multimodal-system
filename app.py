import streamlit as st
import numpy as np
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Try loading model safely
try:
    from tensorflow.keras.models import load_model
    model = load_model("model/lstm_model.h5", compile=False)
except:
    model = None

# -------------------------------
# IMPORT UTILS
# -------------------------------
from utils.preprocess import prepare_input
from utils.anomaly import detect_anomaly
from utils.digital_twin import simulate_tool_wear
from utils.predictive import predict_failure
from utils.streaming import get_sensor_data
from utils.quantum import quantum_optimize
from utils.image_utils import process_image
from utils.api_integration import fetch_cnc_data
from utils.edge import lightweight_predict

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="AI CNC Dashboard", layout="wide")

# -------------------------------
# LOAD CSS
# -------------------------------
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -------------------------------
# LOAD DATA + SCALER
# -------------------------------
@st.cache_resource
def load_all():
    scaler = joblib.load("model/scaler.save")
    dataset = pd.read_csv("data/cnc_data.csv")
    return scaler, dataset

scaler, dataset = load_all()

# -------------------------------
# TITLE
# -------------------------------
st.title("🤖 AI CNC Multimodal Dashboard")

# -------------------------------
# KPI CARDS
# -------------------------------
st.markdown("## 📊 System Overview")

k1, k2, k3, k4 = st.columns(4)

k1.metric("Data Rows", len(dataset))
k2.metric("Model", "LSTM / Fallback")
k3.metric("Status", "Active")
k4.metric("Mode", "Hybrid")

# -------------------------------
# DATA SOURCE
# -------------------------------
source = st.radio("Select Data Source", [
    "Manual",
    "IoT Simulation",
    "API"
])

# -------------------------------
# INPUT
# -------------------------------
if source == "Manual":
    speed = st.number_input("Cutting Speed", value=100.0)
    feed = st.number_input("Feed Rate", value=0.2)
    depth = st.number_input("Depth", value=1.0)
    temp = st.number_input("Temperature", value=30.0)
    vib = st.number_input("Vibration", value=0.01)

    data_input = [speed, feed, depth, temp, vib]

elif source == "IoT Simulation":
    data_input = get_sensor_data()
    st.info(f"📡 IoT Data: {data_input}")

else:
    api_data = fetch_cnc_data()
    if api_data:
        data_input = api_data
        st.success(f"🌐 API Data: {data_input}")
    else:
        st.error("API failed, using default values")
        data_input = [100, 0.2, 1.0, 30, 0.01]

# -------------------------------
# IMAGE INPUT (ONLY SAFE MODAL)
# -------------------------------
image_file = st.file_uploader("🖼 Upload Tool Image", type=["jpg", "png"])

# -------------------------------
# RUN SYSTEM
# -------------------------------
if st.button("🚀 Run AI System"):

    try:
        # Prepare input
        processed = prepare_input(data_input, scaler)

        # ---------------- AI / FALLBACK ----------------
        if model:
            prediction = model.predict(processed)[0][0]
        else:
            prediction = sum(data_input) / len(data_input)

        st.success(f"🔮 Prediction: {prediction:.4f}")

        # ---------------- EDGE ----------------
        edge_pred = lightweight_predict(data_input)
        st.info(f"⚡ Edge Output: {edge_pred:.4f}")

        # ---------------- DIGITAL TWIN ----------------
        twin = simulate_tool_wear(data_input)
        st.info(f"🧠 Digital Twin: {twin:.4f}")

        # ---------------- MAINTENANCE ----------------
        status = predict_failure(twin)
        st.warning(f"🛠 Maintenance: {status}")

        # ---------------- ANOMALY ----------------
        anomaly, threshold = detect_anomaly(data_input)
        if anomaly:
            st.error(f"🚨 Anomaly Detected! Threshold: {threshold:.2f}")
        else:
            st.success("✅ Normal Operation")

        # ---------------- IMAGE ----------------
        if image_file:
            st.image(image_file, caption="Tool Inspection", use_container_width=True)
            process_image(image_file)

        # ---------------- GRAPH ----------------
        st.subheader("📊 Machine Parameters")

        fig, ax = plt.subplots()
        ax.plot(data_input, marker='o')
        ax.set_title("Parameters Trend")
        st.pyplot(fig)

        # ---------------- QUANTUM ----------------
        opt = quantum_optimize(data_input)
        st.success(f"⚛️ Optimized Value: {opt:.4f}")

    except Exception as e:
        st.error(f"Error: {e}")

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.title("📊 System Status")
st.sidebar.success("System Running")
st.sidebar.info("Safe Deployment Mode")
