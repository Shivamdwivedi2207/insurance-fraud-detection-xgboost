import streamlit as st


def prediction_card(prediction):

    probability = prediction["FraudProbability"]
    score = prediction["RiskScore"]
    category = prediction["RiskCategory"]
    action = prediction["RecommendedAction"]

    if category == "Low Risk":
        icon = "🟢"
    elif category == "Medium Risk":
        icon = "🟡"
    elif category == "High Risk":
        icon = "🟠"
    else:
        icon = "🔴"

    st.markdown(
        f"""
### 🛡 Prediction

Risk Category: {icon} {category}

Fraud Probability: {probability:.2%}

Risk Score: {score}/100

Recommended Action: {action}
"""
    )