# ================================
# IMPORTS (SAFE)
# ================================
import streamlit as st
import pandas as pd
import numpy as np
import time

# ================================
# CONFIG
# ================================
st.set_page_config(page_title="AI CNC Futuristic Dashboard", layout="wide")

# ================================
# SCI-FI STYLE
# ================================
st.markdown("""
<style>
body {
    background-color: #0f1117;
    color: white;
}
.block {
    background: #151821;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 0 10px rgba(0,255,255,0.2);
}
</style>
""", unsafe_allow_html=True)

# ================================
# HEADER
# ================================
st.title("⚡ AI CNC FUTURE SYSTEM")
st.write("🔮 Live Monitoring • Simulation • Prediction")

# ================================
# SIDEBAR CONTROL
# ================================
st.sidebar.title("⚙️ Control Panel")

mode = st.sidebar.selectbox("Mode", ["Upload Data", "Live Simulation"])

refresh = st.sidebar.slider("Refresh Speed (sec)", 1, 5, 2)

# ================================
# LIVE SIMULATION MODE
# ================================
if mode == "Live Simulation":

    st.subheader("📡 Real-Time CNC Simulation")

    chart = st.line_chart()
    status_box = st.empty()

    data = []

    for i in range(50):
        new_value = np.random.uniform(20, 100)
        data.append(new_value)

        chart.add_rows(pd.DataFrame([new_value]))

        # Prediction (simple future estimation)
        future = new_value * np.random.uniform(1.05, 1.15)

        # Status
        if new_value > 85:
            status = "⚠️ High Load"
        else:
            status = "✅ Normal"

        status_box.markdown(f"""
        ### 🔧 Current Value: {new_value:.2f}
        ### 🔮 Future Prediction: {future:.2f}
        ### 🚨 Status: {status}
        """)

        time.sleep(refresh)

# ================================
# UPLOAD MODE
# ================================
else:

    st.subheader("📂 Upload CNC Data")

    file = st.file_uploader("Upload CSV", type=["csv"])

    if file:
        try:
            df = pd.read_csv(file)

            st.dataframe(df)

            num_df = df.select_dtypes(include=['number'])

            if not num_df.empty:

                col = st.selectbox("Select Parameter", num_df.columns)

                st.line_chart(num_df[col])

                # Prediction
                current = np.mean(num_df.iloc[0])
                future = current * 1.1

                c1, c2, c3 = st.columns(3)

                c1.metric("Current", f"{current:.2f}")
                c2.metric("Future", f"{future:.2f}")
                c3.metric("Efficiency", f"{np.random.randint(85,100)}%")

                # Suggestion
                if current > np.mean(num_df.values):
                    st.warning("⚠️ Reduce cutting speed")
                else:
                    st.success("✅ Optimal parameters")

            else:
                st.warning("No numeric data")

        except Exception as e:
            st.error(f"Error: {e}")

# ================================
# FOOTER
# ================================
st.sidebar.success("⚡ System Active")
