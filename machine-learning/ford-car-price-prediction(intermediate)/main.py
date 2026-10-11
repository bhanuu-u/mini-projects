import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')


# ============================================================
#                       LOAD DATASET
# ============================================================

df = pd.read_csv("project_3/ford.csv")


# ============================================================
#                     BASIC DATA EXPLORATION
# ============================================================

# print(df.shape)
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())


# ============================================================
#                  EXPLORATORY DATA ANALYSIS (EDA)
# ============================================================

# Price distribution
# sns.histplot(df['price'], bins=50, kde=True)
# plt.show()

# Correlation heatmap
# sns.heatmap(df.corr(numeric_only=True), annot=True)
# plt.show()

# Year vs Price
# sns.boxplot(data=df, x='year', y='price', palette='rainbow')
# plt.xticks(rotation=90)
# plt.show()

# Mileage vs Price
# sns.scatterplot(data=df, x='mileage', y='price')
# plt.show()

# Engine Size vs Price
# sns.boxplot(data=df, x='engineSize', y='price', palette='rainbow')
# plt.show()

# Transmission vs Price
# sns.boxplot(data=df, x='transmission', y='price', palette='rainbow')
# plt.show()

# Fuel Type vs Price
# sns.boxplot(data=df, x='fuelType', y='price', palette='rainbow')
# plt.show()

# Model vs Price
# sns.boxplot(data=df, x='model', y='price', palette='rainbow')
# plt.xticks(rotation=90)
# plt.show()


# ============================================================
#                    PREPARE FEATURES AND TARGET
# ============================================================

X = df.drop(columns=['price'])
y = df['price']


# ============================================================
#                     MODEL 1: ONE-HOT ENCODING
# ============================================================

# Convert categorical columns into dummy variables
X_one_encoded = pd.get_dummies(
    X,
    columns=['model', 'transmission', 'fuelType'],
    drop_first=True,
    dtype=int
)

# Scale numerical columns
from sklearn.preprocessing import StandardScaler

numerical_cols = ['year', 'mileage', 'tax', 'mpg', 'engineSize']

scaler_one_hot = StandardScaler()

X_one_encoded[numerical_cols] = scaler_one_hot.fit_transform(
    X_one_encoded[numerical_cols]
)

print("One-Hot Encoded Data:")
print(X_one_encoded)


# ============================================================
#                    MODEL 2: LABEL ENCODING
# ============================================================

from sklearn.preprocessing import LabelEncoder

categorical_cols = ['model', 'transmission', 'fuelType']

X_label_encoded = X.copy()
label_encoders = {}

# Convert categorical values into numerical labels
for col in categorical_cols:
    encoder = LabelEncoder()

    X_label_encoded[col] = encoder.fit_transform(
        X_label_encoded[col].astype(str)
    )

    label_encoders[col] = encoder


# Scale numerical and label-encoded columns
cols_to_scale = [
    'model', 'year', 'transmission', 'mileage',
    'fuelType', 'tax', 'mpg', 'engineSize'
]

scaler_label = StandardScaler()

X_label_encoded[cols_to_scale] = scaler_label.fit_transform(
    X_label_encoded[cols_to_scale]
)

print("\nLabel Encoded Data:")
print(X_label_encoded)


# ============================================================
#                  IMPORT MODEL AND EVALUATION TOOLS
# ============================================================

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# ============================================================
#       MODEL 1: LINEAR REGRESSION WITH ONE-HOT ENCODING
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X_one_encoded,
    y,
    test_size=0.33,
    random_state=42
)

model_one_hot = LinearRegression()
model_one_hot.fit(X_train, y_train)

y_pred_one_hot = model_one_hot.predict(X_test)

r2_one_hot = r2_score(y_test, y_pred_one_hot)

n = X_test.shape[0]
p = X_test.shape[1]

adjusted_r2_one_hot = 1 - (
    (1 - r2_one_hot) * (n - 1)
) / (n - p - 1)

mae_one_hot = mean_absolute_error(y_test, y_pred_one_hot)
mse_one_hot = mean_squared_error(y_test, y_pred_one_hot)
rmse_one_hot = np.sqrt(mse_one_hot)


# ============================================================
#         MODEL 2: LINEAR REGRESSION WITH LABEL ENCODING
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X_label_encoded,
    y,
    test_size=0.33,
    random_state=42
)

model_label = LinearRegression()
model_label.fit(X_train, y_train)

y_pred_label = model_label.predict(X_test)

r2_label = r2_score(y_test, y_pred_label)

n = X_test.shape[0]
p = X_test.shape[1]

adjusted_r2_label = 1 - (
    (1 - r2_label) * (n - 1)
) / (n - p - 1)

mae_label = mean_absolute_error(y_test, y_pred_label)
mse_label = mean_squared_error(y_test, y_pred_label)
rmse_label = np.sqrt(mse_label)


# ============================================================
#                    COMPARE MODEL PERFORMANCE
# ============================================================

results = pd.DataFrame({
    'Encoding': ['One-Hot Encoding', 'Label Encoding'],
    'R2 Score': [r2_one_hot, r2_label],
    'Adjusted R2': [adjusted_r2_one_hot, adjusted_r2_label],
    'MAE': [mae_one_hot, mae_label],
    'MSE': [mse_one_hot, mse_label],
    'RMSE': [rmse_one_hot, rmse_label]
})

print("\nModel Performance Comparison:")
print(results.to_string(index=False))
