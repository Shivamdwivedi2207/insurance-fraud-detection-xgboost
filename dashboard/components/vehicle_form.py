import streamlit as st


def vehicle_form():

    st.markdown("## 🚗 Vehicle Information")

    month = st.selectbox(
        "Month",
        [
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        ]
    )

    week_of_month = st.selectbox(
        "Week Of Month",
        [1, 2, 3, 4, 5]
    )

    day_of_week = st.selectbox(
        "Day Of Week",
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

    make = st.selectbox(
        "Vehicle Make",
        [
            "Accura",
            "BMW",
            "Chevrolet",
            "Dodge",
            "Ferrari",
            "Ford",
            "Honda",
            "Jaguar",
            "Lexus",
            "Mazda",
            "Mecedes",
            "Mercury",
            "Nisson",
            "Pontiac",
            "Porche",
            "Saab",
            "Saturn",
            "Toyota",
            "VW"
        ]
    )

    vehicle_category = st.selectbox(
        "Vehicle Category",
        [
            "Sport",
            "Sedan",
            "Utility"
        ]
    )

    vehicle_price = st.selectbox(
        "Vehicle Price",
        [
            "less than 20000",
            "20000 to 29000",
            "30000 to 39000",
            "40000 to 59000",
            "60000 to 69000",
            "more than 69000"
        ]
    )

    age_of_vehicle = st.selectbox(
        "Age Of Vehicle",
        [
            "new",
            "2 years",
            "3 years",
            "4 years",
            "5 years",
            "6 years",
            "7 years",
            "more than 7"
        ]
    )

    return {

        "Month": month,

        "WeekOfMonth": week_of_month,

        "DayOfWeek": day_of_week,

        "Make": make,

        "VehicleCategory": vehicle_category,

        "VehiclePrice": vehicle_price,

        "AgeOfVehicle": age_of_vehicle

    }