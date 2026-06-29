# ==========================================================
# Insurance Fraud Detection Inference Engine
# ==========================================================

import pandas as pd


# ==========================================================
# Single Prediction
# ==========================================================

def predict_fraud(model, processed_claim):

    probability = model.predict_proba(
        processed_claim
    )[:, 1]

    prediction = (
        probability >= 0.55
    ).astype(int)

    return prediction[0], probability[0]


# ==========================================================
# Batch Prediction
# ==========================================================

def predict_fraud_batch(model, processed_df):

    probabilities = model.predict_proba(
        processed_df
    )[:, 1]

    predictions = (
        probabilities >= 0.55
    ).astype(int)

    return predictions, probabilities


# ==========================================================
# Risk Level
# ==========================================================

def generate_risk_level(probability):

    score = int(
        round(probability * 100)
    )

    if score <= 25:

        category = "Low Risk"
        action = "Auto Approve"

    elif score <= 50:

        category = "Medium Risk"
        action = "Quick Verification"

    elif score <= 75:

        category = "High Risk"
        action = "Manual Investigation"

    else:

        category = "Critical Risk"
        action = "Fraud Investigation Team"

    return score, category, action


# ==========================================================
# Single Claim Pipeline
# ==========================================================

def fraud_detection_pipeline_single(

    processed_claim,
    original_claim,
    model

):

    prediction, probability = predict_fraud(

        model,
        processed_claim

    )

    score, category, action = generate_risk_level(

        probability

    )

    result = {

        "claim": original_claim.iloc[0].to_dict(),

        "prediction": {

            "FraudPrediction": int(
                prediction
            ),

            "FraudProbability": round(
                float(probability),
                4
            ),

            "RiskScore": score,

            "RiskCategory": category,

            "RecommendedAction": action

        }

    }

    return result


# ==========================================================
# Batch Pipeline
# ==========================================================

def fraud_detection_pipeline_batch(

    processed_df,
    original_df,
    model

):

    predictions, probabilities = predict_fraud_batch(

        model,
        processed_df

    )

    results = original_df.copy()

    fraud_prediction = []
    fraud_probability = []
    risk_score = []
    risk_category = []
    recommended_action = []

    for prediction, probability in zip(

        predictions,
        probabilities

    ):

        score, category, action = generate_risk_level(

            probability

        )

        fraud_prediction.append(

            int(prediction)

        )

        fraud_probability.append(

            round(
                float(probability),
                4
            )

        )

        risk_score.append(

            score

        )

        risk_category.append(

            category

        )

        recommended_action.append(

            action

        )

    results["FraudPrediction"] = fraud_prediction

    results["FraudProbability"] = fraud_probability

    results["RiskScore"] = risk_score

    results["RiskCategory"] = risk_category

    results["RecommendedAction"] = recommended_action

    return results


# ==========================================================
# Batch Summary
# ==========================================================

def generate_batch_summary(results):

    return {

        "total_claims": int(len(results)),

        "fraud_detected": int(
            results["FraudPrediction"].sum()
        ),

        "low_risk": int(
            (results["RiskCategory"] == "Low Risk").sum()
        ),

        "medium_risk": int(
            (results["RiskCategory"] == "Medium Risk").sum()
        ),

        "high_risk": int(
            (results["RiskCategory"] == "High Risk").sum()
        ),

        "critical_risk": int(
            (results["RiskCategory"] == "Critical Risk").sum()
        ),

        "average_probability": round(
            float(results["FraudProbability"].mean()),
            4
        )

    }