
import streamlit as st
import pandas as pd
import joblib

# ========================================================
#                    LOAD MODEL
# ========================================================

model = joblib.load('Knn_heart.pkl')
scaler = joblib.load('scaler.pkl')
columns = joblib.load('columns.pkl')


# ========================================================
#                    APP TITLE
# ========================================================

st.title('Heart Disease Prediction ♥️')

st.write(
    'This app predicts whether a person has heart disease '
    'based on their health parameters.'
)

st.markdown(
    'Provided below are the input fields to enter '
    'the health parameters of the person:'
)


# ========================================================
#                    USER INPUTS
# ========================================================

age = st.slider('Age', min_value=1, max_value=100, value=30)

sex = st.selectbox(
    'Sex',
    options=['Male', 'Female']
)

chest_pain_type = st.selectbox(
    'Chest Pain Type',
    options=[
        'Typical Angina',
        'Atypical Angina',
        'Non-Anginal Pain',
        'Asymptomatic'
    ]
)

resting_bp = st.number_input(
    'Resting Blood Pressure (in mm Hg)',
    min_value=0,
    max_value=300,
    value=120
)

Cholesterol = st.number_input(
    'Cholesterol (in mg/dl)',
    min_value=100,
    max_value=600,
    value=200
)

FastingBS = st.selectbox(
    'Fasting Blood Sugar > 120 mg/dl',
    options=['Yes', 'No']
)

RestingECG = st.selectbox(
    'Resting Electrocardiographic Results',
    options=[
        'Normal',
        'ST-T Wave Abnormality',
        'Left Ventricular Hypertrophy'
    ]
)

Max_HR = st.slider(
    'Maximum Heart Rate Achieved',
    min_value=60,
    max_value=220,
    value=150
)

ExerciseAngina = st.selectbox(
    'Exercise Induced Angina',
    options=['Yes', 'No']
)

Oldpeak = st.number_input(
    'Oldpeak (ST depression induced by exercise relative to rest)',
    min_value=0.0,
    max_value=10.0,
    value=1.0,
    step=0.1
)

Slope = st.selectbox(
    'Slope of the Peak Exercise ST Segment',
    options=[
        'Upsloping',
        'Flat',
        'Downsloping'
    ]
)


# ========================================================
#                    PREDICTION
# ========================================================

if st.button('Predict'):

    input_data = pd.DataFrame([{
        'Age': age,
        'Sex': 'M' if sex == 'Male' else 'F',
        'ChestPainType': {
            'Typical Angina': 'TA',
            'Atypical Angina': 'ATA',
            'Non-Anginal Pain': 'NAP',
            'Asymptomatic': 'ASY'
        }[chest_pain_type],
        'RestingBP': resting_bp,
        'Cholesterol': Cholesterol,
        'FastingBS': 1 if FastingBS == 'Yes' else 0,
        'RestingECG': {
            'Normal': 'Normal',
            'ST-T Wave Abnormality': 'ST',
            'Left Ventricular Hypertrophy': 'LVH'
        }[RestingECG],
        'MaxHR': Max_HR,
        'ExerciseAngina': 'Y' if ExerciseAngina == 'Yes' else 'N',
        'Oldpeak': Oldpeak,
        'ST_Slope': {
            'Upsloping': 'Up',
            'Flat': 'Flat',
            'Downsloping': 'Down'
        }[Slope]
    }])

    # Apply one-hot encoding
    input_data = pd.get_dummies(input_data, drop_first=True)

    # Match the training columns and their order
    input_data = input_data.reindex(
        columns=columns,
        fill_value=0
    )

    # Scale the input using the saved scaler
    input_data_scaled = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(input_data_scaled)

    # Display result
    if prediction[0] == 1:

        st.error(
            "High Risk Indicator",
            icon="🚨"
        )

        st.caption(
            "The model detected patterns associated with heart disease. "
            "Please consult a qualified healthcare professional for assessment."
        )

    else:

        st.success(
            "Lower Risk Indicator",
            icon="✅"
        )

        st.caption(
            "The model did not detect a high-risk pattern in the provided data. "
            "This result does not rule out heart disease."
        )
