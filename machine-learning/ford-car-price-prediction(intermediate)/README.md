# Ford Used Car Price Prediction 🚗

## Project Overview

This project focuses on predicting the prices of used Ford cars using Machine Learning. The dataset contains various vehicle attributes, including model, year, transmission, mileage, fuel type, tax, MPG, and engine size.

The project explores data analysis, preprocessing, categorical encoding, feature scaling, and Linear Regression to understand how different approaches affect prediction performance.

## Objectives

- Understand the factors affecting used car prices.
- Perform Exploratory Data Analysis (EDA) to identify patterns and relationships.
- Compare One-Hot Encoding and Label Encoding for categorical variables.
- Apply feature scaling using StandardScaler.
- Build Linear Regression models using both encoding techniques.
- Evaluate and compare the performance of the models.

## Dataset Description

The dataset contains the following features:

| Feature | Description |
|---|---|
| `model` | Ford car model |
| `year` | Year of manufacture |
| `price` | Selling price of the car |
| `transmission` | Transmission type |
| `mileage` | Distance travelled |
| `fuelType` | Type of fuel used |
| `tax` | Vehicle tax |
| `mpg` | Miles per gallon |
| `engineSize` | Engine capacity |

The target variable is `price`, which the models aim to predict.

## Exploratory Data Analysis (EDA)

Explored the dataset using Pandas and visualisation libraries to understand the distribution of prices and the relationship between vehicle features and price.

The analysis included:
- Examining dataset dimensions, data types, and descriptive statistics.
- Checking for missing values.
- Visualising price distribution using a histogram with KDE.
- Analysing numerical feature correlations using a heatmap.
- Studying the relationship between mileage and price using a scatter plot.
- Comparing prices across car years, models, transmission types, fuel types, and engine sizes using box plots.

## Data Preprocessing

### 1. Feature and Target Separation
Separated the dataset into independent features (`X`) and the target variable (`y`), where `price` is the target.

### 2. One-Hot Encoding
Used `pandas.get_dummies()` to convert the `model`, `transmission`, and `fuelType` categorical columns into numerical dummy variables. Applied `drop_first=True` to remove one category from each encoded feature.

### 3. Label Encoding
Used Scikit-learn's `LabelEncoder` to convert categorical values into numerical labels. Stored the encoders for the individual categorical columns.

### 4. Feature Scaling
Applied `StandardScaler` to numerical features to standardise their values. For the label-encoded approach, scaling was also applied to the encoded categorical columns.

## Model Building

Built two Linear Regression models to explore how different categorical encoding techniques affect a regression problem.

### Model 1: Linear Regression with One-Hot Encoding
- Converted categorical variables into dummy columns.
- Scaled numerical features.
- Trained a Linear Regression model using the processed dataset.

### Model 2: Linear Regression with Label Encoding
- Converted categorical variables into numerical labels.
- Scaled the numerical and label-encoded features.
- Trained a separate Linear Regression model using the processed dataset.

Both models used an 80/20-style split configuration with `test_size=0.33` and `random_state=42`, resulting in approximately 67% training data and 33% testing data.

## Model Evaluation

Evaluated both models using the following regression metrics:

- **R² Score:** Measures how much variation in car prices is explained by the model.
- **Adjusted R² Score:** Adjusts the R² score based on the number of features and observations.
- **Mean Absolute Error (MAE):** Measures the average absolute difference between actual and predicted prices.
- **Mean Squared Error (MSE):** Measures the average squared prediction error.
- **Root Mean Squared Error (RMSE):** Represents prediction error on the same scale as the target variable.

These metrics help compare the predictive performance of the two encoding approaches.

## Technologies Used

- **Python** – Programming language
- **Pandas** – Data manipulation and analysis
- **NumPy** – Numerical computations
- **Matplotlib** – Data visualisation
- **Seaborn** – Statistical visualisation
- **Scikit-learn** – Encoding, feature scaling, model training, and evaluation

## Key Learning Outcomes

- Understood the end-to-end workflow of a regression-based Machine Learning project.
- Practised EDA and visualisation techniques on a real-world dataset.
- Learned the differences between One-Hot Encoding and Label Encoding.
- Applied feature scaling to prepare data for model training.
- Built and evaluated Linear Regression models.
- Learned how regression evaluation metrics help assess prediction quality.

## Project Status

**Completed**

## Author

**A Revanth Bhanu**
