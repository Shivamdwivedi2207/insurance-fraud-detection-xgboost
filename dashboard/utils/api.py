import requests

# ==========================================================
# FastAPI Base URL
# ==========================================================

BASE_URL = "http://127.0.0.1:8000"


# ==========================================================
# Single Claim Prediction
# ==========================================================

def predict_single(claim_data):

    response = requests.post(

        f"{BASE_URL}/predict_single",

        json={

            "claim": claim_data

        }

    )

    if response.status_code == 200:

        return response.json()

    return {

        "detail": response.text

    }

# ==========================================================
# Batch Prediction
# ==========================================================

def predict_batch(csv_file):

    files = {

        "file": csv_file

    }

    response = requests.post(

        f"{BASE_URL}/predict_batch",

        files=files

    )

    return response.json()


# ==========================================================
# Search Policy Number
# ==========================================================

def search_claim(policy_number):

    response = requests.get(

        f"{BASE_URL}/claim/{policy_number}"

    )

    return response.json()