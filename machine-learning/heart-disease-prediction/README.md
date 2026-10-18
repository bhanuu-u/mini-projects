# Heart Disease Prediction using Machine Learning

## About the Project

This project uses machine learning to predict the presence of heart disease based on patient health parameters.

It includes data cleaning, exploratory data analysis (EDA), categorical feature encoding, feature scaling, and a comparison of five machine learning classification algorithms. A Streamlit web application provides an interactive interface where users can enter health parameters and receive predictions from the trained K-Nearest Neighbors (KNN) model.

## Live Demo

Try the deployed application here:

**[Heart Disease Prediction App](https://heart-disease-predictor121.streamlit.app/)**

## Features

- Exploratory Data Analysis (EDA)
- Data cleaning and handling of zero values in cholesterol and resting blood pressure
- Categorical feature encoding using Pandas
- Feature scaling using StandardScaler
- Training and comparison of five machine learning classifiers
- Model evaluation using accuracy, F1-score, confusion matrix, and classification report
- Model persistence using Joblib
- Interactive Streamlit frontend for predictions

## Machine Learning Models

The project compares the following classification algorithms:

1. Logistic Regression
2. K-Nearest Neighbors (KNN)
3. Support Vector Machine (SVM)
4. Decision Tree Classifier
5. Gaussian Naive Bayes

The models are evaluated on a test dataset using accuracy and F1-score. Confusion matrices and classification reports provide additional information about their performance.

## Technologies Used

- **Programming Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Web Application:** Streamlit
- **Model Serialization:** Joblib

## Dataset

The project uses `heart.csv`, which contains patient health parameters.

### Input Features

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG Results
- Maximum Heart Rate
- Exercise-Induced Angina
- Oldpeak
- ST Slope

**Target variable:** `HeartDisease`

The target variable uses binary labels to indicate the presence or absence of heart disease in the dataset.

## Project Structure

```text
heart-disease-prediction/
├── heart.csv
├── heart.py
├── frontend.py
├── Knn_heart.pkl
├── scaler.pkl
├── columns.pkl
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/bhanu-u/mini-projects.git
```

### 2. Navigate to the project directory

```bash
cd mini-projects/machine-learning/heart-disease-prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the model comparison script

```bash
python heart.py
```

This script performs data preprocessing, trains and evaluates the classification models, and displays a comparison of their performance.

### 5. Run the Streamlit application

```bash
python -m streamlit run frontend.py
```

Open the local URL displayed in the terminal to interact with the application.

## Model Evaluation

The project uses the following evaluation metrics:

- **Accuracy:** Measures the proportion of correct predictions.
- **F1-score:** Combines precision and recall into a single metric.
- **Confusion Matrix:** Shows correct and incorrect predictions for each class.
- **Classification Report:** Summarizes precision, recall, F1-score, and support for each class.

The model comparison results can be used to evaluate the strengths and limitations of each classifier.

## Future Improvements

- Improve preprocessing by fitting transformations only on training data.
- Tune model hyperparameters to improve performance.
- Add visualizations comparing model performance.
- Improve model interpretability and validation.
- Enhance the user interface and mobile responsiveness.

## Disclaimer

This project is intended for educational purposes only. Its predictions are not a medical diagnosis and should not replace professional medical advice, diagnosis, or treatment. Consult a qualified healthcare professional for medical concerns.

## Author

**A Revanth Bhanu**

GitHub: [@bhanu-u](https://github.com/bhanu-u)
