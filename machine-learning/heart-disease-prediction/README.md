# Heart Disease Prediction using Machine Learning

## About the Project

This project uses machine learning to predict the presence of heart disease based on patient health parameters. It includes data cleaning, exploratory data analysis (EDA), feature encoding, standard scaling, and a comparison of multiple classification algorithms.

A Streamlit web application allows users to enter health parameters and receive a model prediction through an interactive interface.

## Features

- Exploratory Data Analysis (EDA)
- Data cleaning and handling of zero values in cholesterol and resting blood pressure
- Categorical feature encoding using Pandas
- Feature scaling using StandardScaler
- Training and comparison of five machine learning classifiers
- Model evaluation using accuracy, F1-score, confusion matrix, and classification report
- Interactive Streamlit frontend for predictions

## Machine Learning Models

The project compares the following classification algorithms:

1. Logistic Regression
2. K-Nearest Neighbors (KNN)
3. Support Vector Machine (SVM)
4. Decision Tree Classifier
5. Gaussian Naive Bayes

The models are evaluated on a test dataset, and their accuracy and F1-scores are compared to help identify a suitable model.

## Technologies Used

- **Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Web Application:** Streamlit
- **Model Saving:** Joblib

## Dataset

The project uses `heart.csv`, which contains patient health information.

Some of the features include:

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

The target indicates whether heart disease is present, using the dataset's binary labels.

## Project Structure

```text
heart-disease-prediction/
├── heart.csv
├── model_comparison.py
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

### 2. Navigate to the project folder

```bash
cd mini-projects/machine-learning/heart-disease-prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Train and compare the models

```bash
python model_comparison.py
```

This runs the data preprocessing and model comparison workflow.

### 5. Run the Streamlit application

```bash
python -m streamlit run frontend.py
```

Open the local URL displayed in your terminal to use the application.

## Model Evaluation

The models are evaluated using:

- **Accuracy:** Overall proportion of correct predictions.
- **F1-score:** Balance between precision and recall.
- **Confusion Matrix:** Breakdown of correct and incorrect predictions.
- **Classification Report:** Precision, recall, F1-score, and support for each class.

Actual evaluation results can be added here after running the model comparison script.

## Future Improvements

- Improve preprocessing by fitting transformations only on training data.
- Tune model hyperparameters to improve performance.
- Add visualizations comparing model performance.
- Deploy the Streamlit application online.
- Improve model interpretability and validation.

## Disclaimer

This project is intended for educational purposes only. Its predictions are not a medical diagnosis and should not replace professional medical advice or assessment.


## Author
**A Revanth Bhanu**
## Author

**A Revanth Bhanu**
