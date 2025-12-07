"""
Project: BankAccount class for the Application
===========================
Course:   CS 5001
Student:  Dipen Modi

This file contains class and it's functions that will be used to deposit money into user account, withdraw money from user account and check balance of user account.
"""


class BankAccount:
    """BankAccount defines what attributes a bank account should have and what it can do.

    Attributes:
        username, password, name, account, balance

    Example:
        >>> account = BankAccount("user_name", "Password", "Full Name", "BE100", 0.0)
        >>> account.balance
        0.0
        >>> account.name
        'Full Name'
        >>> account.password
        'Password'
        >>> account.username
        'user_name'
        >>> account.account
        'BE100'
    """

    def __init__(self, account_id: str, account_password: str, customer_name: str, account_number: str, account_balance: float) -> None:
        """Initializing a new bank account with the user information.

        Args:
            account_id (str): Username of account holder.
            account_password (str): Password of account holder.
            customer_name (str): Full name of account holder.
            account_number (str): A unique identifier of user's account type.
            account_balance (float): The account balance of user.

        Returns:
            None
        """
        self.username = account_id
        self.password = account_password
        self.name = customer_name
        self.account = account_number
        self.balance = float(account_balance)

    def check_balance(self) -> float:
        """Checks balance in user's bank account.

        Returns:
            float: Returns the current balance in customer's bank account.

        Examples:
            >>> account_1 = BankAccount("JC99", "U_kant_C_Me", "John Cena", "BE099", 0)
            >>> account_2 = BankAccount("RayM", "RM_moon12", "Ray Mysterio", "BE100", 100)

            >>> account_1.check_balance()
            0.0
            >>> account_2.check_balance()
            100.0
        """
        return self.balance

    def deposit(self, amount: float) -> None:
        """
        Deposits money into the account of user.
        Amount must be a positive number.
        Raises error if amount is invalid.

        Args:
            amount (float): The amount user wishes to deposit to his account.
                            Must be positive.

        Returns:
            None

        Examples:
            >>> account = BankAccount("JC99", "U_kant_C_Me", "John Cena", "BE099", 500000)

            >>> account.deposit(250000)
            >>> account.balance
            750000.0

            >>> account.deposit(0)
            Traceback (most recent call last):
                ...
            ValueError: Deposit amount must be positive. Please try again.

            >>> account.deposit(-100)
            Traceback (most recent call last):
                ...
            ValueError: Deposit amount must be positive. Please try again.

            >>> account.deposit(1)
            >>> account.balance
            750001.0

            >>> account.deposit("Hakuna Matata")
            Traceback (most recent call last):
                ...
            TypeError: Deposit amount must be a number. Please try again.

            >>> account.deposit(250000)
            >>> account.balance
            1000001.0
        """
        # if amount is not an integer or float -
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number. Please try again.")

        # if the amount is a non-positive integer -
        if amount <= 0:
            raise ValueError("Deposit amount must be positive. Please try again.")

        # adding the amount to account holder's account balance.
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Withdraws money from the user's account.
            Must be positive. Raises error if amount is invalid.

        Args:
            amount (float): The amount user wishes to withdraw from his account.

        Returns:
            None

        Example:
            >>> account_1 = BankAccount("JC99", "U_kant_C_Me", "John Cena", "BE099", 500000)
            >>> account_2 = BankAccount("RayM", "RM_moon12", "Ray Mysterio", "BE100", 100)

            >>> account_1.withdraw(250000)
            >>> account_1.balance
            250000.0

            >>> account_2.withdraw(0)
            Traceback (most recent call last):
                ...
            ValueError: Withdrawal amount must be positive. Please try again.

            >>> account_1.withdraw(-10000)
            Traceback (most recent call last):
                ...
            ValueError: Withdrawal amount must be positive. Please try again.

            >>> account_1.withdraw("Hakuna Matata")
            Traceback (most recent call last):
                ...
            TypeError: Withdrawal amount must be a number. Please try again.

            >>> account_2.withdraw(1000)
            Traceback (most recent call last):
                ...
            ValueError: Insufficient funds. Balance: $100.00, Attempted withdrawal: $1000.00
        """
        # if amount is not an integer or float -
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdrawal amount must be a number. Please try again.")

        # if the amount is a non-positive integer -
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive. Please try again.")

        # if there withdrawal amount > balance in account -
        if amount > self.balance:
            raise ValueError(f"Insufficient funds. Balance: ${self.balance:.2f}, "
                             f"Attempted withdrawal: ${amount:.2f}")
        self.balance -= amount


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
