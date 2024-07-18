# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Adds the amount to the account balance."""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraws the amount from the account balance if sufficient funds are available."""
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
    """Prints the current balance in a user-friendly format with two decimal places."""
    print("Current Balance: ${:.2f}".format(self.account_balance))


