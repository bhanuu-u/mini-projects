import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')


# ========================================================
# ===================== LOAD DATA ========================
# ========================================================

df = pd.read_csv('insurance.csv')


# ========================================================
# ========================= EDA ==========================
# ========================================================

df.shape

df.head()

df.info()

df.describe()

df.isnull().sum()

df.columns


# Distribution of numerical columns

numeric_columns = ['age', 'bmi', 'children', 'charges']

for col in numeric_columns:
    plt.figure(figsize=(6, 4))
    sns.histplot(df[col], kde=True, bins=20)
    plt.show()


# Count plot for children

sns.countplot(x=df['children'])
plt.show()


# Count plot for sex

sns.countplot(x=df['sex'])
plt.show()


# Count plot for smoker

sns.countplot(x=df['smoker'])
plt.show()


# Box plots

for col in numeric_columns:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=df[col])
    plt.show()


# Correlation heatmap

plt.figure(figsize=(8, 6))
sns.heatmap(
    df.corr(numeric_only=True),
    annot=True
)
plt.show()


# ========================================================
# =============== DATA CLEANING ==========================
# ========================================================

df_cleaned = df.copy()

df_cleaned.head()

df_cleaned.shape


# Remove duplicate rows

df_cleaned.drop_duplicates(inplace=True)

df_cleaned.shape


# Check missing values

df_cleaned.isnull().sum()


# Check data types

df_cleaned.dtypes


# ========================================================
# =================== ENCODING SEX ========================
# ========================================================

df_cleaned['sex'].value_counts()

df_cleaned['sex'] = df_cleaned['sex'].map({
    "male": 0,
    "female": 1
})

df_cleaned.head()


# ========================================================
# ================= ENCODING SMOKER ======================
# ========================================================

df_cleaned['smoker'].value_counts()

df_cleaned['smoker'] = df_cleaned['smoker'].map({
    "no": 0,
    "yes": 1
})

df_cleaned


# Rename columns

df_cleaned.rename(
    columns={
        'sex': 'is_female',
        'smoker': 'is_smoker'
    },
    inplace=True
)

df_cleaned.head()


# ========================================================
# ================= ENCODING REGION ======================
# ========================================================

df['region'].value_counts()


df_cleaned = pd.get_dummies(
    df_cleaned,
    columns=['region'],
    drop_first=True
)

df_cleaned.head()


# Convert boolean columns into integers

df_cleaned = df_cleaned.astype(int)

df_cleaned


# ========================================================
# ================= FEATURE ENGINEERING ==================
# ========================================================

sns.histplot(df['bmi'])
plt.show()


# Create BMI categories

df_cleaned['bmi_category'] = pd.cut(
    df_cleaned['bmi'],
    bins=[0, 18.5, 24.9, 29.9, float('inf')],
    labels=[
        'Underweight',
        'Normal',
        'Overweight',
        'Obese'
    ]
)

df_cleaned


# Convert BMI categories into dummy variables

df_cleaned = pd.get_dummies(
    df_cleaned,
    columns=['bmi_category'],
    drop_first=True
)


# Convert boolean columns into integers

df_cleaned = df_cleaned.astype(int)

df_cleaned.head()

df_cleaned.columns


# ========================================================
# =================== STANDARD SCALING ===================
# ========================================================

from sklearn.preprocessing import StandardScaler

cols = ['age', 'bmi', 'children']

scaler = StandardScaler()

df_cleaned[cols] = scaler.fit_transform(
    df_cleaned[cols]
)

df_cleaned.head()


# ========================================================
# ============== PEARSON CORRELATION =====================
# ========================================================

from scipy.stats import pearsonr


# List of features to check against target

selected_features = [
    'age',
    'bmi',
    'children',
    'is_female',
    'is_smoker',
    'region_northwest',
    'region_southeast',
    'region_southwest',
    'bmi_category_Normal',
    'bmi_category_Overweight',
    'bmi_category_Obese'
]


# Calculate Pearson correlation

correlations = {}

for feature in selected_features:
    correlations[feature] = pearsonr(
        df_cleaned[feature],
        df_cleaned['charges']
    )[0]


# Create dataframe

correlation_df = pd.DataFrame(
    list(correlations.items()),
    columns=[
        'Feature',
        'Pearson Correlation'
    ]
)


# Sort correlation values

correlation_df = correlation_df.sort_values(
    by='Pearson Correlation',
    ascending=False
)


print(correlation_df)


# ========================================================
# ================= CATEGORICAL FEATURES =================
# ========================================================

cat_features = [
    'is_female',
    'is_smoker',
    'region_northwest',
    'region_southeast',
    'region_southwest',
    'bmi_category_Normal',
    'bmi_category_Overweight',
    'bmi_category_Obese'
]


# ========================================================
# ================= CHI-SQUARE TEST ======================
# ========================================================

from scipy.stats import chi2_contingency

alpha = 0.05


# Divide charges into 4 groups

df_cleaned['charges_bin'] = pd.qcut(
    df_cleaned['charges'],
    q=4,
    labels=False
)


chi2_results = {}


for col in cat_features:

    contingency = pd.crosstab(
        df_cleaned[col],
        df_cleaned['charges_bin']
    )

    chi2_stat, p_val, _, _ = chi2_contingency(
        contingency
    )

    decision = (
        'Reject Null (Keep Feature)'
        if p_val < alpha
        else 'Accept Null (Drop Feature)'
    )

    chi2_results[col] = {
        'chi2_statistic': chi2_stat,
        'p_value': p_val,
        'Decision': decision
    }


chi2_df = pd.DataFrame(
    chi2_results
).T


chi2_df = chi2_df.sort_values(
    by='p_value'
)


print(chi2_df)


# ========================================================
# =================== FINAL FEATURES =====================
# ========================================================

final_df = df_cleaned[
    [
        'age',
        'is_female',
        'bmi',
        'children',
        'is_smoker',
        'charges',
        'region_southeast',
        'bmi_category_Obese'
    ]
]


final_df


# Original dataframe

df