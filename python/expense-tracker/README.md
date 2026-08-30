# Expense Tracker

A Python-based Expense Tracker that allows users to record, manage, analyze, and visualize their expenses.

This project started as a simple expense management application and was gradually extended with JSON file handling, CRUD operations, Pandas-based analysis, and data visualizations.

## Features

- Add expenses
- View all expenses
- Edit existing expenses
- Delete expenses
- Store expenses permanently using JSON
- Automatically record expense dates
- Calculate total spending
- Analyze daily spending
- Analyze monthly spending
- Analyze yearly spending
- Analyze spending by category
- Find highest spending
- Find lowest spending
- Generate a spending summary
- Create different visualizations

## Analysis

The Analysis section provides:

1. Daily Spending
2. Monthly Spending
3. Yearly Spending
4. Spending by Category
5. Highest Spending
6. Lowest Spending
7. Spending Summary
8. Visualizations

The analysis functions are separated into a dedicated `analysis.py` file.

## Visualizations

The project includes different charts to understand spending patterns and distributions.

The visualization functions are separated into a dedicated `visualizations.py` file.

Visualizations include:

- Line graphs for spending trends
- Category comparison charts
- Category distribution charts
- Expense distribution
- Expense comparison visualizations

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- JSON
- File Handling
- Datetime

## Project Structure

```text
expense-tracker/
│
├── expense_tracker.py
├── expenses.json
├── analysis.py
├── visualizations.py
└── README.md
