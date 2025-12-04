# class: Bank Account to deposit money into user account, withdraw money from user account and check balance of user account.

class BankAccount:
    """A class that defines what attributes a bank account should have and defines what it can do."""

    def __init__(self, account_id, account_password, customer_name, account_number, account_balance):
        self.username = account_id
        self.password = account_password
        self.name = customer_name
        self.account = account_number
        self.balance = float(account_balance)

    def deposit(self, amount):
        "Deposits money into the account"
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number. Please try again.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive. Please try again.")
        self.balance += amount
        # print(f"Deposited ${amount}. Current balance: {self.balance}")

    def withdraw(self, amount):
        "Withdraws moeny from the account"
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdrawal amount must be a number. Please try again.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive. Please try again.")
        if amount > self.balance:
            raise ValueError(f"Insufficient funds. Balance: ${self.balance:.2f}, "
                             f"Attempted withdrawal: ${amount:.2f}")
        self.balance -= amount
        # print(f"Withdrawal ${amount} successful! Remaining balance: {self.balance}")

    def check_balance(self):
        return self.balance