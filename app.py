st.header("📂 Upload CNC Data")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        import pandas as pd

        data = pd.read_csv(uploaded_file)

        st.subheader("📊 Uploaded Data")
        st.dataframe(data)

        # -------------------------------
        # SAFE NUMERIC FILTER
        # -------------------------------
        numeric_data = data.select_dtypes(include=['number'])

        if numeric_data.empty:
            st.warning("⚠️ No numeric data found for analysis")
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

            col = st.selectbox("Select column", numeric_data.columns)
            st.line_chart(numeric_data[col])

            # -------------------------------
            # SAFE PREDICTION
            # -------------------------------
            st.subheader("🤖 AI Output")

            sample = numeric_data.iloc[0].values

            # fallback safe prediction
            prediction = sum(sample) / len(sample)

            st.success(f"🔮 Predicted Value: {prediction:.4f}")

            st.metric("AI Output", f"{prediction:.3f}")

    except Exception as e:
        st.error(f"❌ Error reading file: {e}")
