# Expense Tracker

A Python-based Expense Tracker that allows users to record, manage, analyze, and visualize their expenses.

This project was built step by step, starting with basic expense management and gradually adding JSON storage, CRUD operations, Pandas-based analysis, and data visualizations.

---

## Features

- Add new expenses
- View all expenses
- Edit existing expenses
- Delete expenses
- Automatically record expense dates
- Store expenses permanently using JSON
- Calculate total spending
- View spending by category
- Daily spending analysis
- Monthly spending analysis
- Yearly spending analysis
- Highest spending analysis
- Lowest spending analysis
- Spending summary
- Multiple data visualizations
- Separate analysis module
- Separate visualization module
- Loading effects using the time module

---

## Main Menu

    ===================================
           EXPENSE TRACKER
    ===================================
    1. Add Expense
    2. View Expenses
    3. Total Spending
    4. Spending by Category
    5. Delete Expense
    6. Edit Expense
    7. Analysis
    8. Exit
    ===================================

---

## Analysis

The Analysis section provides different ways to understand spending patterns.

    ===================================
              ANALYSIS
    ===================================
    1. Daily Spending
    2. Monthly Spending
    3. Yearly Spending
    4. Spending by Category
    5. Highest Spending
    6. Lowest Spending
    7. Spending Summary
    8. Visualizations
    9. Back to Main Menu
    ===================================

### Analysis Features

- Daily Spending
- Monthly Spending
- Yearly Spending
- Spending by Category
- Highest Spending
- Lowest Spending
- Spending Summary

The analysis functionality is implemented separately in `analysis.py`.

---

## Visualizations

The project includes multiple visualizations to understand spending patterns and distributions.

The visualization functionality is implemented separately in `visualizations.py`.

Visualizations include:

- Daily spending trends
- Monthly spending trends
- Yearly spending trends
- Spending by category
- Category distribution
- Expense amount distribution
- Expense comparisons

---

## CRUD Operations

The Expense Tracker supports the basic CRUD operations.

### Create

Users can add new expenses by entering:

- Category
- Description
- Amount

The current date is automatically added to the expense.

### Read

Users can view all stored expenses along with:

- Category
- Description
- Amount
- Date

### Update

Users can edit:

- Category
- Description
- Amount
- Date

### Delete

Users can select an expense and remove it from the stored data.

---

## Data Storage

Expense data is stored in a JSON file.

Example:

    [
        {
            "date": "2026-08-30",
            "category": "food",
            "description": "outing",
            "amount": 450
        }
    ]

Using JSON allows the expense data to remain available even after the program is closed.

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- JSON
- OS
- Datetime
- Time

---

## Project Structure

    expense-tracker/
    │
    ├── expense_tracker.py
    ├── expenses.json
    ├── analysis.py
    ├── visualizations.py
    └── README.md

### expense_tracker.py

The main application file.

It contains the menu system and handles:

- Adding expenses
- Viewing expenses
- Editing expenses
- Deleting expenses
- Total spending
- Spending by category
- Analysis menu
- Visualization menu
- Saving and loading JSON data

### expenses.json

Stores the expense records and provides persistent storage for the application.

### analysis.py

Contains the functions used to analyze the expense data using Pandas.

### visualizations.py

Contains the functions used to generate charts and graphs using Matplotlib and Seaborn.

---

## How to Run

### 1. Install Python

Make sure Python is installed on your system.

### 2. Install Required Libraries

    pip install pandas matplotlib seaborn

### 3. Run the Application

    python expense_tracker.py

---

## Concepts Practiced

This project helped me practice:

- Python functions
- Lists
- Dictionaries
- Loops
- Conditional statements
- User input
- File handling
- JSON
- CRUD operations
- Exception handling
- Date handling
- Pandas DataFrames
- `groupby()`
- Data aggregation
- Matplotlib
- Seaborn
- Data visualization
- Python modules
- Importing functions between files
- Menu-driven applications
- `time.sleep()`
- Modular Python programming

---

## Development Progress

### Phase 1 - Basic Expense Tracker

- Add expenses
- View expenses
- Store expense information

### Phase 2 - JSON Storage

- Load expenses from JSON
- Save expenses to JSON
- Persistent data storage

### Phase 3 - CRUD Operations

- Create expenses
- Read expenses
- Update expenses
- Delete expenses

### Phase 4 - Expense Analysis

- Total spending
- Spending by category
- Daily spending
- Monthly spending
- Yearly spending
- Highest spending
- Lowest spending
- Spending summary

### Phase 5 - Data Visualization

- Matplotlib visualizations
- Seaborn visualizations
- Separate `visualizations.py` module
- Multiple charts for spending analysis

### Phase 6 - Project Organization

- Separate analysis module
- Separate visualization module
- Organized project structure
- Project documentation

---

## Future Improvements

- Budget tracking
- Monthly budget limits
- Date-range filtering
- Expense search
- Expense filtering
- CSV export
- Excel export
- More advanced visualizations
- Interactive dashboards
- SQL database integration
- Graphical User Interface
- Web application version

---

## Author

**Revanth Bhanu**

Built as a Python mini-project to practice Python programming, file handling, CRUD operations, data analysis, and data visualization.
