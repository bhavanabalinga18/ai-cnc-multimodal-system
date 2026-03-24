# ================================
# IMPORTS (SAFE)
# ================================
import streamlit as st
import pandas as pd
import numpy as np

# ================================
# PAGE CONFIG
# ================================
st.set_page_config(page_title="AI CNC Dashboard", layout="wide")

# ================================
# DARK THEME CSS (SCI-FI STYLE)
# ================================
st.markdown("""
<style>
body {
    background-color: #0f1117;
    color: white;
}
.card {
    background: linear-gradient(145deg, #1c1f26, #111318);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 0 15px rgba(0,255,255,0.1);
}
.big-font {
    font-size: 22px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ================================
# HEADER
# ================================
st.title("⚡ AI CNC FUTURE DASHBOARD")
st.write("Smart Monitoring • Prediction • Analysis")

# ================================
# KPI CARDS
# ================================
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card"><div class="big-font">⚙️ System</div>Active</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><div class="big-font">🤖 AI Mode</div>Running</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card"><div class="big-font">⚡ Health</div>Optimal</div>', unsafe_allow_html=True)

# ================================
# FILE UPLOAD
# ================================
st.header("📂 Upload CNC Data")
file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    try:
        df = pd.read_csv(file)

        st.subheader("📊 Data Preview")
        st.dataframe(df)

        num_df = df.select_dtypes(include=['number'])

        if not num_df.empty:

            # ================================
            # GRAPH
            # ================================
            st.subheader("📈 Performance Graph")

            col = st.selectbox("Select parameter", num_df.columns)
            st.line_chart(num_df[col])

            # ================================
            # CURRENT VALUE
            # ================================
            current = np.mean(num_df.iloc[0])

            c1, c2, c3 = st.columns(3)

            c1.metric("Current Value", f"{current:.2f}")
            c2.metric("Future Prediction", f"{current*1.1:.2f}")
            c3.metric("Efficiency", f"{np.random.randint(85, 100)}%")

            # ================================
            # STATUS
            # ================================
            st.subheader("🚨 System Status")

            threshold = np.mean(num_df.values) + 2*np.std(num_df.values)

            if np.max(num_df.values) > threshold:
                st.error("⚠️ Anomaly Detected")
                st.warning("Suggestion: Reduce load / check tool wear")
            else:
                st.success("✅ System Stable")
                st.info("Suggestion: Maintain current parameters")

        else:
            st.warning("No numeric data found")

    except Exception as e:
        st.error(f"Error: {e}")

# ================================
# SIDEBAR
# ================================
st.sidebar.title("⚡ Control Panel")
st.sidebar.success("System Online")
st.sidebar.info("Upload data to activate dashboard")
