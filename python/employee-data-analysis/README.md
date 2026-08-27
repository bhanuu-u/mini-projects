# Employee Data Analysis — Pandas, Regex & Matplotlib

A data cleaning and exploratory data analysis project built using **Python, Pandas, Regular Expressions (Regex), and Matplotlib**.

The project takes messy employee data, extracts structured information using Regex, cleans and validates the data using Pandas, saves the cleaned dataset, and finally performs exploratory data analysis through visualizations.

---

## 🚀 Project Overview

Real-world datasets are often messy and unstructured.

This project demonstrates a complete data-processing workflow:

**Raw Data → Regex Extraction → Data Cleaning → Type Conversion → Date Conversion → Data Validation → Clean DataFrame → EDA**

The main goal is to practice handling imperfect data and transforming it into a clean, analysis-ready dataset.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** — Data loading, manipulation and cleaning
* **Regex (`re`)** — Extracting structured information from messy text
* **Matplotlib** — Data visualization and exploratory analysis
* **CSV** — Input and cleaned output data storage

---

## 🔄 Project Pipeline

```text
                    RAW DATA
                        │
                        ▼
               Load CSV with Pandas
                        │
                        ▼
              ┌──────────────────┐
              │ Regex Extraction │
              └──────────────────┘
                        │
          Employee ID, Name, Age,
          Salary, Email, Phone...
                        │
                        ▼
                 Data Cleaning
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
       Remove        Clean text    Clean phone
       commas
          │
          ▼
              Type Conversion
                 │         │
                 ▼         ▼
              Age → int  Salary → int
                        │
                        ▼
                 Date Conversion
                        │
                        ▼
                 Data Validation
              │           │           │
              ▼           ▼           ▼
           Missing     Duplicates   Duplicate IDs
                        │
                        ▼
                 Clean DataFrame
                        │
                        ▼
                 Save Clean CSV
                        │
                        ▼
                    EDA / Charts
```

---

## 📋 Workflow Explanation

### 1. Load Raw Data

The raw employee dataset is loaded using Pandas.

```python
df = pd.read_csv("regex_employee_extraction_dataset.csv")
```

The raw data contains messy and inconsistently formatted information that needs to be processed before analysis.

---

### 2. Regex Extraction

Regular Expressions are used to extract structured employee information from the raw text.

Information extracted includes:

* Employee ID
* Employee Name
* Age
* Salary
* Email
* Phone Number
* Other relevant fields

Regex allows patterns to be identified even when the original data is inconsistently formatted.

---

### 3. Data Cleaning

The extracted data is cleaned before analysis.

Cleaning operations include:

* Removing unnecessary commas from salary values
* Cleaning text fields
* Cleaning phone numbers
* Handling inconsistent formatting

---

### 4. Type Conversion

Columns are converted into appropriate data types.

Examples:

```text
Age     → int
Salary  → int
```

Correct data types make the dataset easier to analyze and prevent calculation errors.

---

### 5. Date Conversion

Date fields are converted into proper date/datetime formats so that they can be used for analysis and sorting.

---

### 6. Data Validation

The cleaned dataset is checked for common data-quality issues.

Validation includes:

* Missing values
* Duplicate rows
* Duplicate Employee IDs

This ensures that the final dataset is reliable and suitable for analysis.

---

### 7. Clean DataFrame

After extraction, cleaning, conversion, and validation, the result is a structured and analysis-ready Pandas DataFrame.

---

### 8. Save Clean Dataset

The cleaned dataset is exported as:

```text
cleaned_employee_data.csv
```

This allows the processed data to be reused without repeating the entire cleaning process.

---

### 9. Exploratory Data Analysis

The cleaned data is analyzed using **Matplotlib**.

Charts are used to explore employee-related patterns and relationships in the dataset.

Examples include:

* Salary distribution
* Employee counts
* Age-related analysis
* Department comparisons
* Other relevant employee trends

---

## 📁 Project Structure

```text
employee-data-analysis/
│
├── main.py
│
├── regex_employee_extraction_dataset.csv
│
├── cleaned_employee_data.csv
│
└── README.md
```

### Files

| File                                    | Description                                                             |
| --------------------------------------- | ----------------------------------------------------------------------- |
| `main.py`                               | Main Python program containing extraction, cleaning, validation and EDA |
| `regex_employee_extraction_dataset.csv` | Raw employee dataset                                                    |
| `cleaned_employee_data.csv`             | Cleaned and validated dataset                                           |
| `README.md`                             | Project documentation                                                   |

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate into the project

```bash
cd employee-data-analysis
```

### 3. Install dependencies

```bash
pip install pandas matplotlib
```

### 4. Run the project

```bash
python main.py
```

---

## 🎯 Key Learning Outcomes

Through this project, I practiced:

* Reading CSV files using Pandas
* Extracting structured data using Regex
* Cleaning messy datasets
* Handling inconsistent text and phone numbers
* Removing formatting characters from numerical data
* Converting data types
* Working with dates
* Detecting missing values
* Detecting duplicate records
* Detecting duplicate IDs
* Saving cleaned datasets
* Performing exploratory data analysis
* Creating visualizations using Matplotlib

---

## 📊 Project Workflow

```text
Raw Dataset
     ↓
Pandas
     ↓
Regex Extraction
     ↓
Data Cleaning
     ↓
Type Conversion
     ↓
Date Conversion
     ↓
Data Validation
     ↓
Clean Dataset
     ↓
Matplotlib EDA
```

---

## 💡 Why This Project?

This project was built to practice a realistic data-analysis workflow rather than working with an already-clean dataset.

It demonstrates how raw, messy data can be transformed into structured and analysis-ready data using Python.

---

## 👨‍💻 Author

**Revanth Bhanu**

B.Tech — Computer Science & Data Science

---

⭐ If you find this project useful, consider giving the repository a star!
