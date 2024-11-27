class Expense:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

    def __repr__(self):
        return f"Category: {self.category}, Amount: {self.amount}, Date: {self.date}"
import datetime
import json

# Function to add a new expense
def add_expense(expenses):
    amount = float(input("Enter the amount: "))
    category = input("Enter the category (e.g., groceries, rent, entertainment): ")
    date = input("Enter the date (YYYY-MM-DD) or leave blank for today: ")
    
    # Use today's date if no date is provided
    if not date:
        date = str(datetime.date.today())
    
    expense = Expense(amount, category, date)
    expenses.append(expense.__dict__)  # Storing as dict to easily save to JSON later
    print("Expense added!")

# Function to view all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses to show.")
    else:
        for expense in expenses:
            print(f"{expense['date']}: {expense['category']} - ${expense['amount']}")

# Function to calculate and display the summary
def show_summary(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return

    summary = {}
    
    for expense in expenses:
        category = expense['category']
        if category not in summary:
            summary[category] = []
        summary[category].append(expense['amount'])
    
    print("Expense Summary:")
    for category, amounts in summary.items():
        total = sum(amounts)
        avg = total / len(amounts)
        print(f"Category: {category} | Total: ${total:.2f} | Average: ${avg:.2f}")

# Save expenses to a file
def save_expenses(expenses):
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file)
    print("Expenses saved to file.")

# Load expenses from a file
def load_expenses():
    try:
        with open('expenses.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Main program loop
def main():
    expenses = load_expenses()  # Load previously saved expenses if any
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. Show summary")
        print("4. Save and exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            show_summary(expenses)
        elif choice == '4':
            save_expenses(expenses)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
