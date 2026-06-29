import streamlit as st
import pandas as pd
import plotly.express as px

from utils.api import (
    predict_batch,
    search_claim
)

from components.prediction_card import (
    prediction_card
)


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(

    page_title="Batch Prediction",

    page_icon="📂",

    layout="wide"

)

st.title("📂 Batch Claim Prediction")

st.write(

    "Upload a CSV file containing insurance claims."

)


# ==========================================================
# SESSION STATE
# ==========================================================

if "batch_results" not in st.session_state:

    st.session_state.batch_results = None

if "summary" not in st.session_state:

    st.session_state.summary = None

if "uploaded_name" not in st.session_state:

    st.session_state.uploaded_name = None


# ==========================================================
# FILE UPLOADER
# ==========================================================

uploaded_file = st.file_uploader(

    "Upload Insurance Claims CSV",

    type=["csv"]

)


# ==========================================================
# PREDICT BUTTON
# ==========================================================

predict_button = st.button(

    "🚀 Predict All Claims",

    use_container_width=True,

    type="primary"

)


# ==========================================================
# API CALL
# ==========================================================

if predict_button:

    if uploaded_file is None:

        st.warning(

            "Please upload a CSV first."

        )

    else:

        with st.spinner(

            "Running Fraud Detection..."

        ):

            result = predict_batch(

                uploaded_file

            )

        if "summary" in result:

            st.session_state.summary = result["summary"]

            st.session_state.batch_results = pd.DataFrame(

                result["results"]

            )

            st.session_state.uploaded_name = uploaded_file.name

            st.success(

                "Batch Prediction Completed Successfully."

            )

        else:

            st.error(

                result.get(

                    "detail",

                    "Prediction Failed"

                )

            )


# ==========================================================
# SUMMARY SECTION
# ==========================================================

st.divider()

st.subheader(

    "📈 Prediction Summary"

)

summary = st.session_state.summary

results_df = st.session_state.batch_results

# ==========================================================
# SUMMARY CARDS
# ==========================================================

if summary is not None:

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(

            "Total Claims",

            summary["total_claims"]

        )

    with col2:

        st.metric(

            "Fraud Claims",

            summary["fraud_detected"]

        )

    with col3:

        st.metric(

            "Critical Risk",

            summary["critical_risk"]

        )

    with col4:

        st.metric(

            "Average Probability",

            f"{summary['average_probability']:.2%}"

        )

    st.divider()


# ==========================================================
# CHARTS
# ==========================================================

if results_df is not None:

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:

        fig = px.pie(

            results_df,

            names="RiskCategory",

            title="Risk Category Distribution"
        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    with chart_col2:

        fig = px.histogram(

            results_df,

            x="FraudProbability",

            nbins=20,

            title="Fraud Probability Distribution"
        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    st.divider()


# ==========================================================
# SEARCH SECTION
# ==========================================================

st.subheader(

    "🔍 Search by Policy Number"

)

search_col1, search_col2 = st.columns([4,1])

with search_col1:

    policy_number = st.number_input(

        "Policy Number",

        min_value=1,

        step=1

    )

with search_col2:

    st.write("")

    st.write("")

    search_button = st.button(

        "Search",

        use_container_width=True

    )

st.divider()

# ==========================================================
# SEARCH RESULT
# ==========================================================

if search_button:

    if results_df is None:

        st.warning(

            "Please upload and predict a CSV first."

        )

    else:

        with st.spinner(

            "Searching Claim..."

        ):

            result = search_claim(

                int(policy_number)

            )

        if "claim" in result:

            claim = result["claim"]

            prediction = result["prediction"]

            left_col, right_col = st.columns(

                [2, 1]

            )

            with left_col:

                st.subheader(

                    "📄 Claim Details"

                )

                st.dataframe(

                    pd.DataFrame(

                        claim.items(),

                        columns=[

                            "Field",

                            "Value"

                        ]

                    ),

                    use_container_width=True,

                    hide_index=True

                )

            with right_col:

                st.subheader(

                    "🛡 Prediction"

                )

                prediction_card(

                    prediction

                )

        else:

            st.error(

                result.get(

                    "detail",

                    "Policy Number Not Found"

                )

            )


# ==========================================================
# DOWNLOAD RESULTS
# ==========================================================

if results_df is not None:

    st.divider()

    st.subheader(

        "⬇ Download Prediction Report"

    )

    csv = results_df.to_csv(

        index=False

    ).encode(

        "utf-8"

    )

    st.download_button(

        label="📥 Download CSV",

        data=csv,

        file_name="fraud_prediction_results.csv",

        mime="text/csv",

        use_container_width=True

    )


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.caption(

    "Insurance Fraud Detection Dashboard • Powered by XGBoost + FastAPI + Streamlit"

)