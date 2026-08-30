import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def prepare_dataframe(expenses):

    if not expenses:
        print("No expenses found.")
        return None

    df = pd.DataFrame(expenses)

    df["date"] = pd.to_datetime(df["date"])

    return df


# 1. Expense Amount vs Day of Month
def expense_day_scatter(expenses):

    df = prepare_dataframe(expenses)

    if df is None:
        return

    df["day"] = df["date"].dt.day

    plt.figure(figsize=(10, 5))

    sns.scatterplot(
        data=df,
        x="day",
        y="amount",
        hue="category",
        s=80
    )

    plt.title("Expense Amount vs Day of Month")
    plt.xlabel("Day of Month")
    plt.ylabel("Expense Amount")

    plt.tight_layout()
    plt.show()


# 2. Expense Distribution
def expense_distribution(expenses):

    df = prepare_dataframe(expenses)

    if df is None:
        return

    plt.figure(figsize=(10, 5))

    sns.histplot(
        data=df,
        x="amount",
        bins=15,
        kde=True
    )

    plt.title("Distribution of Expense Amounts")
    plt.xlabel("Expense Amount")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()


# 3. Category Comparison
def category_comparison(expenses):

    df = prepare_dataframe(expenses)

    if df is None:
        return

    category_data = (
        df.groupby("category")["amount"]
        .sum()
        .reset_index()
        .sort_values("amount", ascending=False)
    )

    plt.figure(figsize=(10, 5))

    sns.barplot(
        data=category_data,
        x="category",
        y="amount",
        hue="category",
        legend=False
    )

    plt.title("Category Spending Comparison")
    plt.xlabel("Category")
    plt.ylabel("Total Spending")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


# 4. Category Share
def category_share(expenses):

    df = prepare_dataframe(expenses)

    if df is None:
        return

    category_data = (
        df.groupby("category")["amount"]
        .sum()
    )

    plt.figure(figsize=(8, 8))

    plt.pie(
        category_data.values,
        labels=category_data.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Category Share of Total Spending")

    plt.tight_layout()
    plt.show()


# 5. Expense Amount by Category
def expense_boxplot(expenses):

    df = prepare_dataframe(expenses)

    if df is None:
        return

    plt.figure(figsize=(10, 6))

    sns.boxplot(
        data=df,
        x="category",
        y="amount",
        hue="category",
        legend=False
    )

    plt.title("Expense Amount Distribution by Category")
    plt.xlabel("Category")
    plt.ylabel("Expense Amount")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()