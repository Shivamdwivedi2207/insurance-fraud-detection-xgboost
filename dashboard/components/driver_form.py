import streamlit as st


def driver_form():

    st.markdown("## 👤 Driver Information")

    sex = st.selectbox(
        "Gender",
        [
            "Male",
            "Female"
        ]
    )

    marital_status = st.selectbox(
        "Marital Status",
        [
            "Single",
            "Married",
            "Divorced",
            "Widow"
        ]
    )

    age = st.number_input(
        "Age",
        min_value=16,
        max_value=100,
        value=30,
        step=1
    )

    age_of_policy_holder = st.selectbox(
        "Age Of Policy Holder",
        [
            "16 to 17",
            "18 to 20",
            "21 to 25",
            "26 to 30",
            "31 to 35",
            "36 to 40",
            "41 to 50",
            "51 to 65",
            "over 65"
        ]
    )

    return {

        "Sex": sex,

        "MaritalStatus": marital_status,

        "Age": age,

        "AgeOfPolicyHolder": age_of_policy_holder

    }