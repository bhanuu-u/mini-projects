import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. LOAD RAW DATA
# ============================================================

df = pd.read_csv("regex_employee_extraction_dataset.csv")

cleaned_data = pd.DataFrame()


# ============================================================
# 2. DATA EXTRACTION
# ============================================================

# Employee ID
cleaned_data["Employee_ID"] = df["raw_data"].str.extract(
    r"EMP-(\d+)"
)

# Employee Name
cleaned_data["Name"] = df["raw_data"].str.extract(
    r"\|\s*([A-Za-z ]+)\s*\|"
)

# Age
cleaned_data["Age"] = df["raw_data"].str.extract(
    r"Age\s*:\s*(\d+)"
)

# Salary
cleaned_data["Salary"] = df["raw_data"].str.extract(
    r"Salary\s*:\s*(?:₹|Rs\.|INR)\s*([0-9,]+)"
)

# Department
cleaned_data["Department"] = df["raw_data"].str.extract(
    r"Dept\s*:\s*([A-Za-z]+)"
)

# Location
cleaned_data["Location"] = df["raw_data"].str.extract(
    r"Location\s*:\s*([A-Za-z]+)"
)

# Email
cleaned_data["Email"] = df["raw_data"].str.extract(
    r"Email\s*:\s*([A-Za-z0-9@.]+)"
)

# Mobile Number
cleaned_data["Mobile_Number"] = df["raw_data"].str.extract(
    r"Phone\s*:\s*([^|]+)"
)

# Role
cleaned_data["Role"] = df["raw_data"].str.extract(
    r"Role\s*:\s*([A-Za-z ]+)"
)

# Joining Date
cleaned_data["Joining_Date"] = df["raw_data"].str.extract(
    r"Joined\s*:\s*([0-9\-A-Za-z/]+)"
)


# ============================================================
# 3. DATA CLEANING & TYPE CONVERSION
# ============================================================

# Remove unnecessary spaces from text columns
text_columns = [
    "Name",
    "Department",
    "Location",
    "Email",
    "Role"
]

for col in text_columns:
    cleaned_data[col] = cleaned_data[col].str.strip()


# Clean mobile numbers
cleaned_data["Mobile_Number"] = (
    cleaned_data["Mobile_Number"]
    .str.replace(r"\D", "", regex=True)
    .str[-10:]
)


# Clean salary
cleaned_data["Salary"] = (
    cleaned_data["Salary"]
    .str.replace(",", "", regex=False)
    .astype(int)
)


# Convert age to integer
cleaned_data["Age"] = cleaned_data["Age"].astype(int)


# Convert joining date
cleaned_data["Joining_Date"] = pd.to_datetime(
    cleaned_data["Joining_Date"],
    format="mixed"
)


# ============================================================
# 4. DATA VALIDATION
# ============================================================

print("\nMissing Values:")
print(cleaned_data.isna().sum())

print("\nDuplicate Rows:")
print(cleaned_data.duplicated().sum())

print("\nDuplicate Employee IDs:")
print(cleaned_data["Employee_ID"].duplicated().sum())

print("\nData Types:")
print(cleaned_data.dtypes)


# ============================================================
# 5. SAVE CLEAN DATA
# ============================================================

cleaned_data.to_csv(
    "cleaned_employee_data.csv",
    index=False
)

print("\nCleaned Data:")
print(cleaned_data.head())


# ============================================================
# 6. DATA VISUALIZATION
# ============================================================


# ------------------------------------------------------------
# 6.1 Salary Distribution
# ------------------------------------------------------------

plt.figure(figsize=(8, 6))

plt.hist(
    cleaned_data["Salary"],
    bins=10
)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.show()


# ------------------------------------------------------------
# 6.2 Average Salary by Department
# ------------------------------------------------------------

avg_salary_department = (
    cleaned_data
    .groupby("Department")["Salary"]
    .mean()
)

plt.figure(figsize=(8, 6))

plt.bar(
    avg_salary_department.index,
    avg_salary_department.values
)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.xticks(rotation=30)

plt.show()


# ------------------------------------------------------------
# 6.3 Employee Distribution by Department
# ------------------------------------------------------------

department_count = cleaned_data["Department"].value_counts()

plt.figure(figsize=(8, 8))

plt.pie(
    department_count.values,
    labels=department_count.index,
    autopct="%1.1f%%",
    colors=[
        "red",
        "blue",
        "green",
        "orange",
        "purple",
        "yellow"
    ]
)

plt.title("Employee Distribution by Department")

plt.show()


# ------------------------------------------------------------
# 6.4 Average Salary by Role
# ------------------------------------------------------------

avg_salary_role = (
    cleaned_data
    .groupby("Role")["Salary"]
    .mean()
    .sort_values()
)

plt.figure(figsize=(10, 6))

plt.barh(
    avg_salary_role.index,
    avg_salary_role.values
)

plt.title("Average Salary by Role")
plt.xlabel("Average Salary")
plt.ylabel("Role")

plt.show()

# ----------------------------------------------------------------------------------------------------------------
#                                                         THE PROJECT PIPELINE IS
# ----------------------------------------------------------------------------------------------------------------
                    # RAW DATA
    #                    │
    #                    ▼
    #           Load CSV with Pandas
    #                    │
    #                    ▼
    #           ┌─────────────────┐
    #           │ Regex Extraction│
    #           └─────────────────┘
    #                    │
    #       Employee ID, Name, Age,
    #       Salary, Email, Phone...
    #                    │
    #                    ▼
    #            Data Cleaning
    #                    │
    #       ┌────────────┼────────────┐
    #       ▼            ▼            ▼
    #    Remove       Clean text   Clean phone
    #    commas
    #       │
    #       ▼
    #          Type Conversion
    #       │              │
    #       ▼              ▼
    #     Age → int     Salary → int
    #                    │
    #                    ▼
    #           Date Conversion
    #                    │
    #                    ▼
    #            Data Validation
    #       │             │             │
    #       ▼             ▼             ▼
    #    Missing       Duplicates    Duplicate IDs
    #                    │
    #                    ▼
    #            Clean DataFrame
    #                    │
    #                    ▼
    #           Save Clean CSV
    #                    │
    #                    ▼
    #               EDA / Charts