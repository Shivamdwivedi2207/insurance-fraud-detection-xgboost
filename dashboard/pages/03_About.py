import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About")

st.write(
    """
    **Car Insurance Fraud Detection System** is a machine learning application that predicts
    whether an insurance claim is fraudulent using an optimized **XGBoost** model.
    The system provides both **single claim** and **batch claim** prediction through
    a FastAPI backend and an interactive Streamlit dashboard.
    """
)

st.divider()

st.subheader("🎯 Objective")

st.write(
    """
    Detect potentially fraudulent insurance claims to assist investigators
    in making faster and more informed decisions.
    """
)

st.divider()

st.subheader("⚙ Tech Stack")

st.markdown("""
- **Machine Learning:** XGBoost, Scikit-learn
- **Backend:** FastAPI
- **Frontend:** Streamlit
- **Data Processing:** Pandas, NumPy
- **Model Serialization:** Joblib
""")

st.divider()

st.subheader("🚀 Features")

st.markdown("""
- Single Claim Fraud Prediction
- Batch CSV Prediction
- Policy Number Search
- Fraud Probability Estimation
- Risk Scoring & Recommended Action
""")

st.divider()

st.subheader("📊 Model")

st.markdown("""
- **Algorithm:** XGBoost Classifier
- **Prediction:** Fraud / Genuine Claim
- **Output:** Fraud Probability, Risk Score, Risk Category, Recommended Action
""")

st.divider()

st.caption("Developed as a Production-Level Machine Learning Project.")
