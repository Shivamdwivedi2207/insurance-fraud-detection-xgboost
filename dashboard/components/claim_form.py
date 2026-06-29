import streamlit as st


def claim_form():

    st.markdown("## 📋 Claim Information")

    day_of_week_claimed = st.selectbox(
        "Day Of Week Claimed",
        [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]
    )

    month_claimed = st.selectbox(
        "Month Claimed",
        [
            "Jan","Feb","Mar","Apr","May","Jun",
            "Jul","Aug","Sep","Oct","Nov","Dec"
        ]
    )

    week_of_month_claimed = st.selectbox(
        "Week Of Month Claimed",
        [1,2,3,4,5]
    )

    days_policy_accident = st.selectbox(
        "Days Policy Accident",
        [
            "none",
            "1 to 7",
            "8 to 15",
            "15 to 30",
            "more than 30"
        ]
    )

    days_policy_claim = st.selectbox(
        "Days Policy Claim",
        [
            "none",
            "8 to 15",
            "15 to 30",
            "more than 30"
        ]
    )

    past_number_of_claims = st.selectbox(
        "Past Number Of Claims",
        [
            "none",
            "1",
            "2 to 4",
            "more than 4"
        ]
    )

    police_report_filed = st.selectbox(
        "Police Report Filed",
        [
            "Yes",
            "No"
        ]
    )

    witness_present = st.selectbox(
        "Witness Present",
        [
            "Yes",
            "No"
        ]
    )

    agent_type = st.selectbox(
        "Agent Type",
        [
            "External",
            "Internal"
        ]
    )

    number_of_suppliments = st.selectbox(
        "Number Of Supplements",
        [
            "none",
            "1 to 2",
            "3 to 5",
            "more than 5"
        ]
    )

    address_change_claim = st.selectbox(
        "Address Change Claim",
        [
            "no change",
            "under 6 months",
            "1 year",
            "2 to 3 years",
            "4 to 8 years"
        ]
    )

    number_of_cars = st.selectbox(
        "Number Of Cars",
        [
            "1 vehicle",
            "2 vehicles",
            "3 to 4",
            "5 to 8",
            "more than 8"
        ]
    )

    return {

        "DayOfWeekClaimed": day_of_week_claimed,

        "MonthClaimed": month_claimed,

        "WeekOfMonthClaimed": week_of_month_claimed,

        "Days_Policy_Accident": days_policy_accident,

        "Days_Policy_Claim": days_policy_claim,

        "PastNumberOfClaims": past_number_of_claims,

        "PoliceReportFiled": police_report_filed,

        "WitnessPresent": witness_present,

        "AgentType": agent_type,

        "NumberOfSuppliments": number_of_suppliments,

        "AddressChange_Claim": address_change_claim,

        "NumberOfCars": number_of_cars

    }