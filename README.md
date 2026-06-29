# 🛡 Car Insurance Fraud Detection System

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![XGBoost](https://img.shields.io/badge/XGBoost-Machine%20Learning-success)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green)

A production-oriented Machine Learning application that predicts fraudulent car insurance claims using an optimized **XGBoost Classifier**. The project integrates an end-to-end ML pipeline with a **FastAPI** backend and an interactive **Streamlit** dashboard for both single and batch claim analysis.

---

## 📌 Project Overview

Insurance fraud leads to significant financial losses and increases operational costs for insurance companies. Manual claim verification is time-consuming and often ineffective for handling large volumes of claims.

This project automates fraud detection by estimating the probability that a claim is fraudulent, assigning a risk category, and recommending an appropriate action. It supports both **single claim prediction** and **batch claim analysis**, making it suitable for real-world insurance workflows.

---

## ✨ Features

* 🔍 Single Claim Fraud Prediction
* 📂 Batch Prediction using CSV files
* 📊 Fraud Probability Estimation
* 🎯 Risk Score Generation
* 🚨 Risk Category Classification
* 📑 Recommended Investigation Action
* 🔎 Search Claims by Policy Number
* 🌐 REST API built with FastAPI
* 🖥 Interactive Streamlit Dashboard
* 📥 Download Prediction Reports

---

## 🧠 Machine Learning Pipeline

```text
Raw Insurance Claims
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Optimized XGBoost Classifier
        │
        ▼
Fraud Probability
        │
        ▼
Risk Score & Risk Category
        │
        ▼
Recommended Action
```

---

## ⚙️ Tech Stack

### Machine Learning

* XGBoost
* Scikit-learn
* Pandas
* NumPy

### Backend

* FastAPI
* Uvicorn
* Pydantic

### Frontend

* Streamlit
* Plotly

### Model Serialization

* Joblib

---

## 📂 Project Structure

```text
insurance-fraud-detection-xgboost/

├── app/                  # FastAPI application
├── dashboard/            # Streamlit dashboard
├── services/             # Data preprocessing
├── src/                  # Inference pipeline
├── artifacts/            # Encoders & feature metadata
├── models/               # Trained XGBoost model
├── screenshots/          # Dashboard screenshots
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Dashboard Modules

### 🏠 Home

Provides an overview of the application and quick navigation.

### 🔍 Single Claim Prediction

Predicts fraud for an individual insurance claim and returns:

* Fraud Prediction
* Fraud Probability
* Risk Score
* Risk Category
* Recommended Action

### 📂 Batch Prediction

Upload a CSV containing multiple insurance claims.

Features include:

* Batch prediction
* Summary statistics
* Interactive charts
* Policy Number search
* Download prediction report

### ℹ️ About

Provides information about the project, technology stack, and objectives.

---

## 📡 API Endpoints

| Method | Endpoint                 | Description                          |
| ------ | ------------------------ | ------------------------------------ |
| GET    | `/`                      | Health Check                         |
| POST   | `/predict_single`        | Predict a Single Insurance Claim     |
| POST   | `/predict_batch`         | Predict Multiple Claims              |
| GET    | `/claim/{policy_number}` | Retrieve Prediction by Policy Number |

Interactive API Documentation:

```text
http://localhost:8000/docs
```

---

## 📊 Sample Prediction Output

```json
{
  "prediction": {
    "FraudPrediction": 1,
    "FraudProbability": 0.93,
    "RiskScore": 93,
    "RiskCategory": "Critical Risk",
    "RecommendedAction": "Fraud Investigation Team"
  }
}
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/insurance-fraud-detection-xgboost.git

cd insurance-fraud-detection-xgboost
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run FastAPI

```bash
uvicorn app.main:app --reload
```

API Documentation

```text
http://127.0.0.1:8000/docs
```

---

## ▶️ Run Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

---

## 📷 Dashboard Preview

> Add screenshots after deployment.

```text
screenshots/

home.png

single_prediction.png

batch_prediction.png

about.png
```

---

## 🎯 Business Value

* Automates fraud detection
* Reduces manual investigation effort
* Prioritizes high-risk claims
* Supports faster insurance claim processing
* Improves operational efficiency

---

## 🔮 Future Improvements

* Docker Containerization
* Cloud Deployment
* Database Integration
* User Authentication
* Model Monitoring
* Automated Model Retraining
* CI/CD Pipeline
* MLOps Integration

---

## 👨‍💻 Author

**Shivam Dwivedi**

B.Tech – Artificial Intelligence & Machine Learning

Interested in:

* Machine Learning
* Deep Learning
* Generative AI
* MLOps
* Backend AI Systems

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
