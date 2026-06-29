# ==========================================================
# Insurance Fraud Detection API
# ==========================================================
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from pydantic import BaseModel
import pandas as pd
import joblib

from src.inference import (
    fraud_detection_pipeline_batch,
    fraud_detection_pipeline_single,
    generate_batch_summary,
)
from services.preprocessing import preprocess_claims

# ==========================================================
# Initialize API
# ==========================================================
app = FastAPI(
    title="Insurance Fraud Detection API",
    description="Production ML API",
    version="1.0",
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_ROOT / "models" / "modelsxgboost_final_optimized.pkl"
FEATURE_NAMES_PATH = PROJECT_ROOT / "artifacts" / "feature_names.pkl"
DATASET_PATH = PROJECT_ROOT / "data" / "raw" / "car_claims.csv"

# ==========================================================
# Load Model
# ==========================================================
model = joblib.load(str(MODEL_PATH))

# ==========================================================
# Load Feature Names
# ==========================================================
feature_names = joblib.load(str(FEATURE_NAMES_PATH))

# ==========================================================
# Request Schemas
# ==========================================================
class ClaimData(BaseModel):
    features: list


class SingleClaimRequest(BaseModel):
    claim: dict


# ==========================================================
# Home Route
# ==========================================================
@app.get("/")
def home():
    return {"message": "Insurance Fraud Detection API Running Successfully"}


# ==========================================================
# Legacy Endpoint (97 Features)
# ==========================================================
@app.post("/predict")
def predict_claim(data: ClaimData):
    if len(data.features) != len(feature_names):
        raise HTTPException(
            status_code=400,
            detail=f"Expected {len(feature_names)} features",
        )

    claim_df = pd.DataFrame([data.features], columns=feature_names)
    result = fraud_detection_pipeline_single(claim_df, claim_df, model)
    return result


# ==========================================================
# Single Raw Claim Endpoint
# ==========================================================
@app.post("/predict_single")
def predict_single_claim(data: SingleClaimRequest):
    try:
        raw_df = pd.DataFrame([data.claim])
        processed_df = preprocess_claims(raw_df)
        result = fraud_detection_pipeline_single(processed_df, raw_df, model)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ==========================================================
# Batch Prediction Endpoint
# ==========================================================
@app.post("/predict_batch")
async def predict_batch_claims(file: UploadFile = File(...)):
    try:
        raw_df = pd.read_csv(file.file)
        processed_df = preprocess_claims(raw_df)
        results_df = fraud_detection_pipeline_batch(processed_df, raw_df, model)
        summary = generate_batch_summary(results_df)
        return {
            "summary": summary,
            "results": results_df.to_dict(orient="records"),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ==========================================================
# Claim Lookup Endpoint
# ==========================================================
@app.get("/claim/{policy_number}")
def get_claim(policy_number: int):
    try:
        claims_df = pd.read_csv(DATASET_PATH)
        claim_row = claims_df.loc[claims_df["PolicyNumber"] == int(policy_number)]

        if claim_row.empty:
            raise HTTPException(status_code=404, detail="Policy Number Not Found")

        claim = claim_row.iloc[[0]].copy()
        processed_df = preprocess_claims(claim)
        result = fraud_detection_pipeline_single(processed_df, claim, model)
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))