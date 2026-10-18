
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

warnings.filterwarnings('ignore')


# ========================================================
#                    LOAD DATA
# ========================================================

df = pd.read_csv("basic_project_2/heart.csv")

print(df.head())


# ========================================================
#                       EDA
# ========================================================

# print(df.columns)
# print(df.shape)
# print(df.info())
# print(df.describe())


# Check for duplicate values
print("Duplicate values:", df.duplicated().sum())


# Check target variable distribution
print("\nHeart Disease distribution:")
print(df['HeartDisease'].value_counts())

# df['HeartDisease'].value_counts().plot(kind='bar')
# plt.show()


# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())


# ========================================================
#                   VISUALIZATION
# ========================================================

def plotting(var, num):
    plt.subplot(2, 2, num)
    sns.histplot(df[var], kde=True)
    plt.title(var)


# plotting('Age', 1)
# plotting('RestingBP', 2)
# plotting('Cholesterol', 3)
# plotting('MaxHR', 4)
# plt.tight_layout()
# plt.show()


# ========================================================
#                    DATA CLEANING
# ========================================================

# Checking Cholesterol values
print("\nCholesterol values:")
print(df['Cholesterol'].value_counts())


# Cholesterol cannot realistically be zero,
# so replacing zero values with the mean
ch_mean = df.loc[df['Cholesterol'] != 0, 'Cholesterol'].mean()

df['Cholesterol'] = df['Cholesterol'].replace(0, ch_mean)
df['Cholesterol'] = df['Cholesterol'].round(2)


# Checking RestingBP values
print("\nRestingBP values:")
print(df['RestingBP'].value_counts())


# Resting blood pressure cannot realistically be zero,
# so replacing zero values with the mean
resting_bp_mean = df.loc[df['RestingBP'] != 0, 'RestingBP'].mean()

df['RestingBP'] = df['RestingBP'].replace(0, resting_bp_mean)
df['RestingBP'] = df['RestingBP'].round(2)


# ========================================================
#                MORE VISUALIZATION
# ========================================================

# sns.countplot(x='Sex', hue='HeartDisease', data=df)
# plt.show()

# sns.countplot(x='ChestPainType', hue='HeartDisease', data=df)
# plt.show()

# sns.countplot(x='FastingBS', hue='HeartDisease', data=df)
# plt.show()

# sns.boxplot(x='HeartDisease', y='Cholesterol', data=df)
# plt.show()

# sns.violinplot(x='HeartDisease', y='Age', data=df)
# plt.show()

# sns.heatmap(df.corr(numeric_only=True), annot=True)
# plt.show()


# ========================================================
#                 DATA PREPROCESSING
# ========================================================

# Convert categorical columns into numerical columns
df_encode = pd.get_dummies(df, drop_first=True)

# Convert True/False values into 1/0
df_encode = df_encode.astype(int)

print("\nEncoded Data:")
print(df_encode.head())


# ========================================================
#                   STANDARD SCALING
# ========================================================

num_cols = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']

scaler = StandardScaler()

df_encode[num_cols] = scaler.fit_transform(df_encode[num_cols])

print("\nScaled Data:")
print(df_encode.columns)


# ========================================================
#                TRAIN TEST SPLIT
# ========================================================

x = df_encode.drop("HeartDisease", axis=1)
y = df_encode['HeartDisease']

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=45
)


# ========================================================
#                 MODEL COMPARISON
# ========================================================

scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

models = {
    'logistic_regression': LogisticRegression(),
    'knn': KNeighborsClassifier(),
    'svm': SVC(),
    'decision_tree': DecisionTreeClassifier(),
    'Naive_Bayes': GaussianNB()
}

result = []

for name, model in models.items():

    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    result.append({
        'model': name,
        "accuracy": round(acc, 4),
        "f1 score": round(f1, 4)
    })

    print("\nModel:", name)
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

print("\nFinal Model Comparison:")
print(pd.DataFrame(result).sort_values(
    by="f1 score", ascending=False
).to_string(index=False))

import joblib
joblib.dump(models['knn'],'Knn_heart.pkl')
joblib.dump(scaler,'scaler.pkl')
joblib.dump(x.columns.to_list(),'columns.pkl')