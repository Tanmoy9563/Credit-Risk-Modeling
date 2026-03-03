# ============================================
# Fintech Grade Credit Risk Prediction System
# ============================================

import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# -----------------------------------
# Page Config
# -----------------------------------
st.set_page_config(page_title="Credit Risk App")

# -----------------------------------
# Load Model
# -----------------------------------
model = joblib.load("xgbClassifier_credit_model.pkl")
model_columns = joblib.load("model_columns_.pkl")

# -----------------------------------
# Title
# -----------------------------------
st.title("🏦 Credit Risk Prediction App")
st.markdown("### Enter Applicant Information")
st.divider()

# -----------------------------------
# Input Section (Proper Alignment)
# -----------------------------------

# Row 1 → Age & Sex
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=80, value=30)

with col2:
    sex = st.selectbox("Sex", ["male", "female"])


# Row 2 → Job & Duration
col3, col4 = st.columns(2)

with col3:
    job = st.number_input("Job (0–3)", min_value=0, max_value=3, value=1)

with col4:
    duration = st.number_input("Duration (months)", min_value=1, value=12)


# Row 3 → Credit Amount & Saving Accounts ✅ FIXED
col5, col6 = st.columns(2)

with col5:
    credit_amount = st.number_input("Credit Amount", min_value=0, value=1000)

with col6:
    saving_accounts = st.selectbox("Saving Accounts", ["little", "moderate", "rich"])


# Row 4 → Housing & Checking Account
col7, col8 = st.columns(2)

with col7:
    housing = st.selectbox("Housing", ["own", "rent", "free"])

with col8:
    checking_account = st.selectbox("Checking Account", ["little", "moderate", "rich"])

st.divider()

# -----------------------------------
# Create Input DataFrame
# -----------------------------------
input_df = pd.DataFrame({
    "Age": [age],
    "Sex": [sex],
    "Job": [job],
    "Housing": [housing],
    "Saving accounts": [saving_accounts],
    "checking account": [checking_account],
    "Credit amount": [credit_amount],
    "Duration": [duration]
})

# -----------------------------------
# Prediction
# -----------------------------------
if st.button("🔍 Predict Risk"):

    # Apply same encoding used in training
    input_df = pd.get_dummies(input_df)

    # Add missing columns
    for col in model_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns
    input_df = input_df[model_columns]

    # Prediction
    pred = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    st.divider()
    st.subheader("📊 Prediction Result")

    # Display result
    if pred == 1:
        st.success(f"✅ The predicted credit risk is: **GOOD**")
    else:
        st.error(f"❌ The predicted credit risk is: **BAD**")


