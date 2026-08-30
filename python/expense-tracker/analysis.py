import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def daily_spending(expenses):

    if not expenses:
        print("No expenses found.")
        return

    df = pd.DataFrame(expenses)

    df["date"] = pd.to_datetime(df["date"])

    daily = (
        df.groupby("date")["amount"]
        .sum()
        .reset_index()
    )

    print("\nDaily Spending")
    print("=" * 30)
    print(daily)
    print("=" * 30)
    plt.figure(figsize=(10,6))
    plt.plot(daily["date"],daily["amount"],marker="o",color="orange")
    plt.title("Daily spendings")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def monthly_spending(expenses):

    if not expenses:
        print("No expenses found.")
        return

    df = pd.DataFrame(expenses)

    # Convert date column to datetime
    df["date"] = pd.to_datetime(df["date"])

    # Extract year-month
    df["month"] = df["date"].dt.to_period("M")

    # Calculate total spending for each month
    monthly = (
        df.groupby("month")["amount"]
        .sum()
        .reset_index()
    )

    print("\nMonthly Spending")
    print("=" * 30)
    print(monthly)
    print("=" * 30)

    # Line Graph
    plt.figure(figsize=(10, 5))
    plt.plot(monthly["month"].astype(str),monthly["amount"],marker="o",color="orange")
    plt.title("Monthly Spending")
    plt.xlabel("Month")
    plt.ylabel("Amount Spent")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def yearly_spending(expenses):

    if not expenses:
        print("No expenses found.")
        return

    df = pd.DataFrame(expenses)

    # Convert date column to datetime
    df["date"] = pd.to_datetime(df["date"])

    # Extract year
    df["year"] = df["date"].dt.year

    # Calculate total spending for each year
    yearly = (
        df.groupby("year")["amount"]
        .sum()
        .reset_index()
    )

    print("\nYearly Spending")
    print("=" * 30)
    print(yearly)
    print("=" * 30)

    # Line Graph
    plt.figure(figsize=(10, 5))

    plt.plot(
    yearly["year"].astype(str),yearly["amount"],marker="o",color="Orange")
    plt.title("Yearly Spending")
    plt.xlabel("Year")
    plt.ylabel("Amount Spent")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def category_analysis(expenses):

    if not expenses:
        print("No expenses found.")
        return

    df = pd.DataFrame(expenses)

    category_data = (
        df.groupby("category")["amount"]
        .sum()
        .reset_index()
        .sort_values("amount", ascending=False)
    )

    print("\nSpending by Category")
    print("=" * 30)
    print(category_data)
    print("=" * 30)

    # Bar Graph
    plt.figure(figsize=(10, 5))
    sns.barplot(x = category_data["category"],y = category_data["amount"],palette="viridis")
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount Spent")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def highest_spending(expenses):

    if not expenses:
        print("No expenses found.")
        return

    df = pd.DataFrame(expenses)

    # Get top 10 expenses
    top_expenses = (
        df.sort_values("amount", ascending=False)
        .head(10)
        .copy()
    )

    print("\nTop 10 Highest Expenses")
    print("=" * 40)
    print(top_expenses[["date", "category", "description", "amount"]])
    print("=" * 40)

    # Create label for each expense
    top_expenses["expense"] = (
        top_expenses["category"]
        + " - "
        + top_expenses["description"]
    )

    # Seaborn horizontal bar chart
    plt.figure(figsize=(10, 6))
    sns.barplot(
        x=top_expenses["amount"],
        y=top_expenses["expense"],
        hue=top_expenses["expense"],
        palette="viridis",
        legend=False
    )
    plt.title("Top 10 Highest Expenses")
    plt.xlabel("Amount Spent")
    plt.ylabel("Expense")
    plt.tight_layout()
    plt.show()


def lowest_spending(expenses):

    if not expenses:
        print("No expenses found.")
        return

    df = pd.DataFrame(expenses)

    # Get 10 lowest expenses
    lowest_expenses = (
        df.sort_values("amount", ascending=True)
        .head(10)
        .copy()
    )

    print("\nTop 10 Lowest Expenses")
    print("=" * 40)
    print(lowest_expenses[["date", "category", "description", "amount"]])
    print("=" * 40)

    # Create label for each expense
    lowest_expenses["expense"] = (
        lowest_expenses["category"]
        + " - "
        + lowest_expenses["description"]
    )

    # Seaborn horizontal bar chart
    plt.figure(figsize=(10, 6))

    sns.barplot(
        x=lowest_expenses["amount"],
        y=lowest_expenses["expense"],
        hue=lowest_expenses["expense"],
        palette="viridis",
        legend=False
    )

    plt.title("Top 10 Lowest Expenses")
    plt.xlabel("Amount Spent")
    plt.ylabel("Expense")

    plt.tight_layout()
    plt.show()


def spending_summary(expenses):

    if not expenses:
        print("No expenses found.")
        return

    df = pd.DataFrame(expenses)

    # Convert date to datetime
    df["date"] = pd.to_datetime(df["date"])

    # Basic statistics
    total_spending = df["amount"].sum()
    average_expense = df["amount"].mean()
    highest_expense = df["amount"].max()
    lowest_expense = df["amount"].min()
    number_of_expenses = len(df)

    # Category with highest spending
    category_totals = df.groupby("category")["amount"].sum()
    highest_category = category_totals.idxmax()
    highest_category_amount = category_totals.max()

    # Day with highest spending
    daily_totals = df.groupby("date")["amount"].sum()
    highest_spending_day = daily_totals.idxmax()
    highest_day_amount = daily_totals.max()

    print("\n")
    print("=" * 40)
    print("          SPENDING SUMMARY")
    print("=" * 40)

    print("Total Spending          :", total_spending)
    print("Average Expense         :", round(average_expense, 2))
    print("Highest Expense         :", highest_expense)
    print("Lowest Expense          :", lowest_expense)
    print("Number of Expenses      :", number_of_expenses)

    print("-" * 40)

    print("Highest Spending Category:", highest_category)
    print("Category Spending       :", highest_category_amount)

    print("Highest Spending Day    :", highest_spending_day.date())
    print("Day Spending            :", highest_day_amount)

    print("=" * 40)    