import streamlit as st
import pandas as pd

from components.vehicle_form import vehicle_form
from components.policy_form import policy_form
from components.driver_form import driver_form
from components.claim_form import claim_form
from components.prediction_card import prediction_card
from utils.build_claim import build_claim

from utils.api import predict_single


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Single Claim Prediction",
    page_icon="🔍",
    layout="wide"
)


# ==========================================================
# Title
# ==========================================================

st.title("🔍 Single Claim Prediction")

st.write(
    "Fill all claim details below and use the action buttons to predict, review, or reset."
)


# ==========================================================
# Input Form
# ==========================================================

vehicle_data = vehicle_form()

st.divider()

policy_data = policy_form()

st.divider()

driver_data = driver_form()

st.divider()

claim_data = claim_form()

st.divider()

predict_button = st.button(
    "🚀 Predict Fraud",
    use_container_width=True,
    type="primary"
)

st.write("")

result_placeholder = st.empty()

complete_claim = build_claim(
    vehicle_data,
    policy_data,
    driver_data,
    claim_data
)

if predict_button:
    with st.spinner("Predicting Fraud..."):
        result = predict_single(complete_claim)

    with result_placeholder:
        if "prediction" in result:
            prediction = result["prediction"]
            prediction_card(prediction)
        else:
            st.error("Prediction Failed")
            st.code(result)
