# expense_manager.py
# Handles daily expenses

class ExpenseManager:
    def __init__(self):
        self.expenses = []  # Each item: (name, amount)

    def add_expense(self, name, amount):
        # Store expenses manually
        entry = (name, amount)
        self.expenses.append(entry)

    def get_total(self):
        # Manual sum (no built-in sum)
        total = 0
        for item in self.expenses:
            total = total + item[1]
        return total

    def get_all_expenses(self):
        return self.expenses
