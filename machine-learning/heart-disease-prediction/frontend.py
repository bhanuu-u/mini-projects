
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Load saved files
BASE_DIR = Path(__file__).resolve().parent

model = joblib.load(BASE_DIR / 'Knn_heart.pkl')
scaler = joblib.load(BASE_DIR / 'scaler.pkl')
columns = joblib.load(BASE_DIR / 'columns.pkl')

st.title("Heart Disease Prediction ❤️")
st.markdown("Provide the following details to check your heart disease risk.")

# Collect user input
age = st.slider("Age", 18, 100, 40)
sex = st.selectbox("Sex", ["M", "F"])
chest_pain = st.selectbox(
    "Chest Pain Type", ["ATA", "NAP", "TA", "ASY"]
)
resting_bp = st.number_input(
    "Resting Blood Pressure (mm Hg)", 80, 200, 120
)
cholesterol = st.number_input(
    "Cholesterol (mg/dL)", 100, 600, 200
)
fasting_bs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dL", [0, 1]
)
resting_ecg = st.selectbox(
    "Resting ECG", ["Normal", "ST", "LVH"]
)
max_hr = st.slider("Max Heart Rate", 60, 220, 150)
exercise_angina = st.selectbox(
    "Exercise-Induced Angina", ["Y", "N"]
)
oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

if st.button("Predict"):

    # Create input using the original dataset categories
    raw_input = pd.DataFrame([{
        "Age": age,
        "Sex": sex,
        "ChestPainType": chest_pain,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "RestingECG": resting_ecg,
        "MaxHR": max_hr,
        "ExerciseAngina": exercise_angina,
        "Oldpeak": oldpeak,
        "ST_Slope": st_slope
    }])

    # Apply the same one-hot encoding used during training
    input_df = pd.get_dummies(raw_input, drop_first=True)

    # Match the exact training column names and order
    input_df = input_df.reindex(columns=columns, fill_value=0)

    # Scale the input using the saved scaler
    scaled_input = scaler.transform(input_df)

    # Predict
    prediction = model.predict(scaled_input)[0]

    if prediction == 1:
        st.error("⚠️ High Risk Indicator")
        st.caption(
            "The model detected patterns associated with heart disease. "
            "Please consult a qualified healthcare professional for assessment."
        )
    else:
        st.success("✅ Lower Risk Indicator")
        st.caption(
            "This result does not rule out heart disease or replace "
            "professional medical advice."
        )
