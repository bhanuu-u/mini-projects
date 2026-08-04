import json
import time
import os

FILE_NAME = "employee.json"


def load_data():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump([], f, indent=4)
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_data(emp):
    with open(FILE_NAME, "w") as f:
        json.dump(emp, f, indent=4)


def loading(msg):
    print(msg, end="", flush=True)
    for _ in range(3):
        time.sleep(0.2)
        print(".", end="", flush=True)
    print()


def display(emp):
    if not emp:
        print("\nNo employees found.\n")
        return

    print("\n" + "=" * 55)
    print("EMPLOYEE LIST")
    print("=" * 55)
    for e in emp:
        print(f"ID         : {e['id']}")
        print(f"Name       : {e['name']}")
        print(f"Salary     : {e['salary']}")
        print(f"Department : {e['department']}")
        print("-" * 55)


def add_employee(emp):
    emp_id = input("Enter ID: ")

    for e in emp:
        if e["id"] == emp_id:
            print("Employee ID already exists!")
            return

    name = input("Enter Name: ")
    salary = int(input("Enter Salary: "))
    department = input("Enter Department: ")

    emp.append({
        "id": emp_id,
        "name": name,
        "salary": salary,
        "department": department
    })

    save_data(emp)
    print(f"{name} added successfully.")


def search_employee(emp):
    emp_id = input("Enter Employee ID: ")
    loading("Searching")

    for e in emp:
        if e["id"] == emp_id:
            print("\nEmployee Found")
            print("-" * 30)
            print(f"ID         : {e['id']}")
            print(f"Name       : {e['name']}")
            print(f"Salary     : {e['salary']}")
            print(f"Department : {e['department']}")
            return

    print("Employee not found.")


def update_salary(emp):
    emp_id = input("Enter Employee ID: ")

    for e in emp:
        if e["id"] == emp_id:
            new_salary = int(input("Enter New Salary: "))
            e["salary"] = new_salary
            save_data(emp)
            print("Salary updated successfully.")
            return

    print("Employee not found.")


def delete_employee(emp):
    emp_id = input("Enter Employee ID: ")

    for e in emp:
        if e["id"] == emp_id:
            emp.remove(e)
            save_data(emp)
            print("Employee deleted successfully.")
            return

    print("Employee not found.")


def total_employees(emp):
    print(f"\nTotal Employees : {len(emp)}")


def highest_paid(emp):
    if not emp:
        print("No employees found.")
        return

    highest = max(emp, key=lambda x: x["salary"])

    print("\nHighest Paid Employee")
    print("-" * 30)
    print(f"Name       : {highest['name']}")
    print(f"Salary     : {highest['salary']}")
    print(f"Department : {highest['department']}")


def statistics(emp):
    if not emp:
        print("No employees found.")
        return

    salaries = [e["salary"] for e in emp]

    print("\nEmployee Statistics")
    print("-" * 35)
    print(f"Highest Salary : {max(salaries)}")
    print(f"Lowest Salary  : {min(salaries)}")
    print(f"Average Salary : {sum(salaries)/len(salaries):.2f}")


def menu():
    emp = load_data()

    while True:
        print("\n" + "=" * 60)
        print("        EMPLOYEE MANAGEMENT SYSTEM")
        print("=" * 60)
        print("1. Display Employees")
        print("2. Add Employee")
        print("3. Search Employee")
        print("4. Update Salary")
        print("5. Delete Employee")
        print("6. Total Employees")
        print("7. Highest Paid Employee")
        print("8. Salary Statistics")
        print("9. Exit")
        print("=" * 60)

        choice = input("Enter your choice: ")

        if choice == "1":
            display(emp)

        elif choice == "2":
            add_employee(emp)

        elif choice == "3":
            search_employee(emp)

        elif choice == "4":
            update_salary(emp)

        elif choice == "5":
            delete_employee(emp)

        elif choice == "6":
            total_employees(emp)

        elif choice == "7":
            highest_paid(emp)

        elif choice == "8":
            statistics(emp)

        elif choice == "9":
            print("\nThank you for using Employee Management System!")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    menu()
