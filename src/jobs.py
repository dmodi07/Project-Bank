# jobs.py

# Characters:
#1 Felonious Gru
#2 Joseph Nefario
#3 Stuart D'Minion
#4 Dave D'Minion
#5 Bob D'Minion
#6 Vector Perkins
#7 El Macho
#8 Scarlet Overkill
#9 Maxime Le Mal
#10 Jean Clawed
#11 Wild Knuckles
#12 Eduardo Perez


class BankAccount:
    """A class that defines what attributes a bank account should have and defines what it can do."""

    def __init__(self, customer_name, account_number, account_balance):
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

    def check_balance(self):
        return self.balance
        
