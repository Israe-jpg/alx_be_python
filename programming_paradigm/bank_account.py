class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited: ${amount:.2f}")  # Assuming this format is exactly correct

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.2f}")  # Assuming this format is exactly correct
        else:
            print("Insufficient funds.")  # Ensure this matches the expected output exactly

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")



