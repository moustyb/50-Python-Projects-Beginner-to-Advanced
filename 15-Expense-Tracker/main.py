# main.py
import csv
import matplotlib.pyplot as plt

CSV_FILE = "expenses.csv"

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., food, travel, rent): ")
    amount = input("Enter amount: ")
    try:
        amount = float(amount)
        with open(CSV_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([date, category, amount])
        print("Expense added!")
    except ValueError:
        print("Amount must be a number.")

def show_summary():
    expenses = {}
    total = 0
    try:
        with open(CSV_FILE, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) != 3: 
                    continue
                _, category, amount = row
                amount = float(amount)
                total += amount
                expenses[category] = expenses.get(category, 0) + amount
    except FileNotFoundError:
        print("No expenses recorded yet.")
        return

    print("\nExpense Summary:")
    print(f"Total: ${total:.2f}")
    for cat, amt in expenses.items():
        print(f"{cat}: ${amt:.2f}")

    # Visualization
    if expenses:
        plt.bar(expenses.keys(), expenses.values())
        plt.title("Expenses by Category")
        plt.ylabel("Amount ($)")
        plt.show()

def main():
    while True:
        print("\n📊 Expense Tracker")
        print("1. Add Expense")
        print("2. Show Summary")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
