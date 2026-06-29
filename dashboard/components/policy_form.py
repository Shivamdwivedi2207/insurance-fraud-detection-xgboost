import streamlit as st


def policy_form():

    st.markdown("## 📄 Policy Information")

    accident_area = st.selectbox(
        "Accident Area",
        [
            "Urban",
            "Rural"
        ]
    )

    fault = st.selectbox(
        "Fault",
        [
            "Policy Holder",
            "Third Party"
        ]
    )

    policy_type = st.selectbox(
        "Policy Type",
        [
            "Sport - Liability",
            "Sport - Collision",
            "Sport - All Perils",
            "Sedan - Liability",
            "Sedan - Collision",
            "Sedan - All Perils",
            "Utility - Liability",
            "Utility - Collision",
            "Utility - All Perils"
        ]
    )

    base_policy = st.selectbox(
        "Base Policy",
        [
            "Liability",
            "Collision",
            "All Perils"
        ]
    )

    deductible = st.selectbox(
        "Deductible",
        [
            300,
            400,
            500,
            700
        ]
    )

    driver_rating = st.selectbox(
        "Driver Rating",
        [
            1,
            2,
            3,
            4
        ]
    )

    year = st.selectbox(
        "Policy Year",
        [
            1994,
            1995,
            1996
        ]
    )

    return {

        "AccidentArea": accident_area,

        "Fault": fault,

        "PolicyType": policy_type,

        "BasePolicy": base_policy,

        "Deductible": deductible,

        "DriverRating": driver_rating,

        "Year": year

    }