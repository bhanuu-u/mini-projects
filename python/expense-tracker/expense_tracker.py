import pandas as pd
import json
import os
import time
from datetime import date


# ============================================================
# ANALYSIS FUNCTIONS
# ============================================================

from analysis import (
    daily_spending,
    monthly_spending,
    yearly_spending,
    category_analysis,
    highest_spending,
    lowest_spending,
    spending_summary
)


# ============================================================
# VISUALIZATION FUNCTIONS
# ============================================================

from visualizations import (
    expense_day_scatter,
    expense_distribution,
    category_comparison,
    category_share,
    expense_boxplot
)


# ============================================================
# FILE HANDLING
# ============================================================

def load_expenses():

    try:

        file_path = os.path.join(
            os.path.dirname(__file__),
            "expenses.json"
        )

        with open(file_path, "r") as file:
            return json.load(file)

    except FileNotFoundError:

        return []


def save_expenses():

    file_path = os.path.join(
        os.path.dirname(__file__),
        "expenses.json"
    )

    with open(file_path, "w") as file:
        json.dump(expenses, file, indent=4)


expenses = load_expenses()


# ============================================================
# EXPENSE FUNCTIONS
# ============================================================

def add_expense(category, description, amount):

    expense = {
        "date": str(date.today()),
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)


# ============================================================
# DISPLAY FUNCTIONS
# ============================================================

def print_expense(expense, index):

    print(index)
    print("Category    :", expense["category"])
    print("Description :", expense["description"])
    print("Amount      :", expense["amount"])
    print("Date        :", expense["date"])
    print("=" * 30)


def show_all_expenses():

    if not expenses:

        print("No expenses found.")
        return

    for index, expense in enumerate(expenses, start=1):

        print_expense(expense, index)


# ============================================================
# LOADING EFFECT
# ============================================================

def loading_message(message):

    print(message)

    time.sleep(0.5)
    print(".")

    time.sleep(0.5)
    print("..")

    time.sleep(0.5)
    print("...")


# ============================================================
# MAIN PROGRAM
# ============================================================

while True:

    print("\n" + "=" * 35)
    print("       EXPENSE TRACKER")
    print("=" * 35)

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Spending by Category")
    print("5. Delete Expense")
    print("6. Edit Expense")
    print("7. Analysis")
    print("8. Exit")

    print("=" * 35)

    response = int(
        input("Enter your response: ")
    )


    # ========================================================
    # 1. ADD EXPENSE
    # ========================================================

    if response == 1:

        category = input(
            "Enter the category of the expense: "
        )

        description = input(
            "Enter the description for your expense: "
        )

        amount = int(
            input("Enter the amount of your expense: ")
        )

        add_expense(
            category,
            description,
            amount
        )

        save_expenses()

        print("\nExpense added successfully! ✅")

        loading_message("Saving")


    # ========================================================
    # 2. VIEW EXPENSES
    # ========================================================

    elif response == 2:

        print("\n" + "=" * 35)
        print("          ALL EXPENSES")
        print("=" * 35)

        show_all_expenses()

        time.sleep(1)


    # ========================================================
    # 3. TOTAL SPENDING
    # ========================================================

    elif response == 3:

        total = 0

        for expense in expenses:

            total += expense["amount"]

        print("\nTotal Spending:", total)

        time.sleep(1)


    # ========================================================
    # 4. SPENDING BY CATEGORY
    # ========================================================

    elif response == 4:

        if not expenses:

            print("No expenses found.")

        else:

            category_spending = {}

            for expense in expenses:

                category = expense["category"]
                amount = expense["amount"]

                if category in category_spending:

                    category_spending[category] += amount

                else:

                    category_spending[category] = amount


            data = []

            for category, amount in category_spending.items():

                data.append({
                    "category": category,
                    "spending": amount
                })


            df = pd.DataFrame(data)

            print("\n")
            print(df)

        time.sleep(1)


    # ========================================================
    # 5. DELETE EXPENSE
    # ========================================================

    elif response == 5:

        if not expenses:

            print("No expenses found.")

        else:

            print("\n" + "=" * 35)
            print("       DELETE EXPENSE")
            print("=" * 35)

            show_all_expenses()

            expense_number = int(
                input(
                    "\nEnter the expense number to delete: "
                )
            )


            if 1 <= expense_number <= len(expenses):

                deleted_expense = expenses.pop(
                    expense_number - 1
                )

                save_expenses()

                print(
                    "\nExpense deleted successfully! ✅"
                )

                print(
                    "Deleted:",
                    deleted_expense
                )

                loading_message("Deleting")


            else:

                print("Invalid expense number.")

        time.sleep(1)


    # ========================================================
    # 6. EDIT EXPENSE
    # ========================================================

    elif response == 6:

        if not expenses:

            print("No expenses found.")

        else:

            print("\n" + "=" * 35)
            print("         EDIT EXPENSE")
            print("=" * 35)

            show_all_expenses()

            expense_number = int(
                input(
                    "\nEnter the expense number to edit: "
                )
            )


            if 1 <= expense_number <= len(expenses):

                expense = expenses[
                    expense_number - 1
                ]


                print("\nWhat do you want to edit?")

                print("1. Category")
                print("2. Description")
                print("3. Amount")
                print("4. Date")
                print("5. Cancel")


                choice = int(
                    input("\nEnter your choice: ")
                )


                if choice == 1:

                    expense["category"] = input(
                        "Enter the new category: "
                    )


                elif choice == 2:

                    expense["description"] = input(
                        "Enter the new description: "
                    )


                elif choice == 3:

                    expense["amount"] = int(
                        input("Enter the new amount: ")
                    )


                elif choice == 4:

                    expense["date"] = input(
                        "Enter the new date (YYYY-MM-DD): "
                    )


                elif choice == 5:

                    print("Edit cancelled.")

                    continue


                else:

                    print("Invalid choice.")

                    continue


                save_expenses()

                print(
                    "\nExpense updated successfully! ✅"
                )

                loading_message("Updating")


            else:

                print("Invalid expense number.")

        time.sleep(1)


    # ========================================================
    # 7. ANALYSIS
    # ========================================================

    elif response == 7:

        while True:

            print("\n" + "=" * 35)
            print("          ANALYSIS")
            print("=" * 35)

            print("1. Daily Spending")
            print("2. Monthly Spending")
            print("3. Yearly Spending")
            print("4. Spending by Category")
            print("5. Highest Spending")
            print("6. Lowest Spending")
            print("7. Spending Summary")
            print("8. Visualizations")
            print("9. Back to Main Menu")

            print("=" * 35)


            analysis_choice = int(
                input("Enter your choice: ")
            )


            if analysis_choice == 1:

                daily_spending(expenses)


            elif analysis_choice == 2:

                monthly_spending(expenses)


            elif analysis_choice == 3:

                yearly_spending(expenses)


            elif analysis_choice == 4:

                category_analysis(expenses)


            elif analysis_choice == 5:

                highest_spending(expenses)


            elif analysis_choice == 6:

                lowest_spending(expenses)


            elif analysis_choice == 7:

                spending_summary(expenses)


            # =================================================
            # VISUALIZATIONS
            # =================================================

            elif analysis_choice == 8:

                while True:

                    print("\n" + "=" * 40)
                    print("          VISUALIZATIONS")
                    print("=" * 40)

                    print("1. Expense Amount vs Day")
                    print("2. Expense Distribution")
                    print("3. Category Comparison")
                    print("4. Category Share")
                    print("5. Expense Distribution by Category")
                    print("6. Back")

                    print("=" * 40)


                    visualization_choice = int(
                        input("Enter your choice: ")
                    )


                    if visualization_choice == 1:

                        expense_day_scatter(expenses)


                    elif visualization_choice == 2:

                        expense_distribution(expenses)


                    elif visualization_choice == 3:

                        category_comparison(expenses)


                    elif visualization_choice == 4:

                        category_share(expenses)


                    elif visualization_choice == 5:

                        expense_boxplot(expenses)


                    elif visualization_choice == 6:

                        break


                    else:

                        print("Invalid choice.")

            # =================================================
            # BACK TO MAIN MENU
            # =================================================

            elif analysis_choice == 9:

                break


            else:

                print("Invalid choice.")


    # ========================================================
    # 8. EXIT
    # ========================================================

    elif response == 8:

        print("\nSaving your data")

        time.sleep(0.5)
        print(".")

        time.sleep(0.5)
        print("..")

        time.sleep(0.5)
        print("...")

        print("\nThank you for using Expense Tracker! 👋")

        break


    # ========================================================
    # INVALID RESPONSE
    # ========================================================

    else:

        print(
            "\nInvalid Response. Please try again."
        )

        time.sleep(1)