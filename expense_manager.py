import json
from expense import Expense


def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            expense_data = json.load(file)

        expenses = []

        for data in expense_data:
            expense = Expense(
                data["name"],
                data["amount"],
                data["category"]
            )

            expenses.append(expense)

        return expenses

    except FileNotFoundError:
        return []


def save_expenses(expenses):
    expense_data = []

    for expense in expenses:
        data = {
            "name": expense.name,
            "amount": expense.amount,
            "category": expense.category
        }

        expense_data.append(data)

    with open("expenses.json", "w") as file:
        json.dump(expense_data, file, indent=4)


def add_expense(expenses):
    expense_name = input("Enter expense name: ").strip()

    if expense_name == "":
        print("Expense name cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    category = input("Enter category: ").strip()

    if category == "":
        print("Category cannot be empty.")
        return

    expense = Expense(
        expense_name,
        amount,
        category
    )

    expenses.append(expense)

    save_expenses(expenses)

    print("Expense added successfully!")


def view_expenses(expenses):
    print("\n===================================")
    print("          YOUR EXPENSES")
    print("===================================")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("No.   Expense")
    print("------------------------------------------")

    for index, expense in enumerate(expenses, start=1):
        print(index, expense)


def search_expense(expenses):
    search_category = input("Enter category to search: ").strip()

    if search_category == "":
        print("Category cannot be empty.")
        return

    found = False

    for expense in expenses:
        if expense.category.lower() == search_category.lower():
            print(
                expense.name,
                "- ₹",
                expense.amount
            )

            found = True

    if found == False:
        print("No expenses found in this category.")


def total_expenses(expenses):
    total = 0

    for expense in expenses:
        total = total + expense.amount

    print("Total Expenses: ₹", total)


def highest_expense(expenses):
    if len(expenses) == 0:
        print("No expenses available.")
        return

    highest = expenses[0]

    for expense in expenses:
        if expense.amount > highest.amount:
            highest = expense

    print(
        "Highest Expense:",
        highest.name,
        "- ₹",
        highest.amount
    )


def delete_expense(expenses):
    if len(expenses) == 0:
        print("No expenses available.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(
            index,
            expense.name,
            "- ₹",
            expense.amount,
            "-",
            expense.category
        )

    try:
        number = int(input("Enter expense number to delete: "))
    except ValueError:
        print("Invalid number. Please enter a number.")
        return

    if number < 1 or number > len(expenses):
        print("Invalid expense number.")
        return

    deleted_expense = expenses.pop(number - 1)

    save_expenses(expenses)

    print(
        deleted_expense.name,
        "deleted successfully!"
    )


def update_expense(expenses):
    if len(expenses) == 0:
        print("No expenses available.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(
            index,
            expense.name,
            "- ₹",
            expense.amount,
            "-",
            expense.category
        )

    try:
        number = int(input("Enter expense number to update: "))
    except ValueError:
        print("Invalid number. Please enter a number.")
        return

    if number < 1 or number > len(expenses):
        print("Invalid expense number.")
        return

    expense = expenses[number - 1]

    new_name = input("Enter new expense name: ").strip()

    if new_name == "":
        print("Expense name cannot be empty.")
        return

    try:
        new_amount = float(input("Enter new amount: "))

        if new_amount <= 0:
            print("Amount must be greater than 0.")
            return

    except ValueError:
        print("Invalid amount. Update cancelled.")
        return

    new_category = input("Enter new category: ").strip()

    if new_category == "":
        print("Category cannot be empty.")
        return

    expense.update(
        new_name,
        new_amount,
        new_category
    )

    save_expenses(expenses)

    print("Expense updated successfully!")