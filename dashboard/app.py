import streamlit as st

st.set_page_config(
    page_title="Car Insurance Fraud Detection",
    page_icon="🛡",
    layout="wide"
)

# ==========================
# CSS
# ==========================

st.markdown("""
<style>

.main{
    padding-top:1rem;
}

.title{
    text-align:center;
    font-size:60px;
    font-weight:800;
    color:#111827;
    margin-bottom:10px;
}

.description{
    text-align:center;
    font-size:20px;
    color:#4B5563;
    width:75%;
    margin:auto;
    margin-bottom:40px;
    line-height:1.7;
}

.card{
    background:white;
    border-radius:20px;
    padding:35px;
    text-align:center;
    box-shadow:0px 5px 20px rgba(0,0,0,0.08);
    border:1px solid #EEEEEE;
    height:320px;
}

.icon{
    font-size:55px;
}

.card-title{
    font-size:30px;
    font-weight:700;
    margin-top:20px;
}

.card-text{
    font-size:18px;
    color:#555;
    margin-top:25px;
    line-height:1.6;
}

.blue{
    color:#2563EB;
}

.green{
    color:#16A34A;
}

.orange{
    color:#EA580C;
}

</style>

""",unsafe_allow_html=True)

# ==========================
# TITLE
# ==========================

st.markdown(

"""
<div class='title'>

🛡 Car Insurance Fraud Detection System

</div>
""",

unsafe_allow_html=True

)

# ==========================
# DESCRIPTION
# ==========================

st.markdown(

"""
<div class='description'>

This application predicts whether an insurance claim is fraudulent using an optimized <b>XGBoost</b>
machine learning model. Users can analyze individual claims,
perform batch predictions, and search uploaded claims using
the policy number.

</div>
""",

unsafe_allow_html=True

)

st.write("")

st.write("")

# ==========================
# CARDS
# ==========================

col1,col2,col3=st.columns(3,gap="large")

with col1:

    st.markdown("""

<div class='card'>

<div class='icon blue'>🔍</div>

<div class='card-title blue'>

Single Prediction

</div>

<div class='card-text'>

Predict fraud for one insurance claim.

</div>

</div>

""",unsafe_allow_html=True)

with col2:

    st.markdown("""

<div class='card'>

<div class='icon green'>📂</div>

<div class='card-title green'>

Batch Prediction

</div>

<div class='card-text'>

Analyze multiple insurance claims
using a CSV file.

</div>

</div>

""",unsafe_allow_html=True)

with col3:

    st.markdown("""

<div class='card'>

<div class='icon orange'>ℹ️</div>

<div class='card-title orange'>

About

</div>

<div class='card-text'>

Learn more about the project,
model and technology stack.

</div>

</div>

""",unsafe_allow_html=True)