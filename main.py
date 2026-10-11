from expense_manager import (
    load_expenses,
    add_expense,
    view_expenses,
    search_expense,
    total_expenses,
    highest_expense,
    delete_expense,
    update_expense
)


def display_menu():
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Total Expenses")
    print("5. Highest Expense")
    print("6. Delete Expense")
    print("7. Update Expense")
    print("8. Exit")


def main():
    print("===================================")
    print("      PERSONAL EXPENSE TRACKER")
    print("===================================")

    expenses = load_expenses()

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            search_expense(expenses)

        elif choice == "4":
            total_expenses(expenses)

        elif choice == "5":
            highest_expense(expenses)

        elif choice == "6":
            delete_expense(expenses)

        elif choice == "7":
            update_expense(expenses)

        elif choice == "8":
            print("Thank you for using Personal Expense Tracker!")
            break

        else:
            print("Invalid choice. Please select 1 to 8.")


if __name__ == "__main__":
    main()