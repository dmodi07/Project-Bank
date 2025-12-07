"""
jobs.py file contains helper functions for Application
===========================
Course:   CS 5001
Student:  Dipen Modi

This module contains six helper functions to run the banking application:
    1. load_accounts()
    2. save_accounts(accounts: dict)
    3. validate_password(password: str)
    4. generate_account_number(accounts: dict)
    5. authenticate_user(username: str, password: str, accounts: dict)
    6. create_new_account(username: str, password: str, name: str, accounts: dict)

This module handles reading content from database, saving content to database, account number generation for any new clients, banking access upon user authentication, password validation upon login attempts and also the ability to create a new account for new clients.
"""
import json
from bank_account import BankAccount

# CONSTANTS:
BANK_ACRONYM = "BE"         # BE(Bank of Evil): starting part of any account number.
NEW_ACCOUNT_BALANCE = 0.0   # starting balance when a client opens a new bank account.


def load_accounts() -> dict:
    """
    Loads accounts from clients.json and returns dictionary of BankAccount objects.

    Reads clients.json file (client database) and converts the stored data into a dictionary of BankAccount objects. Each username is the Key to it's corresponding BankAccount object (Value).
    If the file doesn't exist, then this function returns an empty dictionary to work with despite 0 clients.

    Returns:
        dict: Dictionary that maps usernames to BankAccount objects.
              Returns empty dictionary if the file doesn't exist.

    Examples:
        >>> accounts = load_accounts()
        >>> isinstance(accounts, dict)
        True
    """
    try:
        # opens and reads contents of the file (clients database)
        with open('clients.json', 'r') as file:
            data = json.load(file)

        # creates an empty dictionary to store BankAccount objects that we create next.
        accounts = {}

        # converts each (key, value) pair into a BankAccount object.
        for username, info in data.items():
            account = BankAccount(
                info["username"],
                info["password"],
                info["name"],
                info["account_number"],
                info["balance"]
            )

            # adding the BankAccount object to the empty dictionary (accounts{}) line 46.
            accounts[username] = account
        return accounts

    except FileNotFoundError:       # returning empty dictionary in case file doesn't exist.
        return {}


def save_accounts(accounts: dict) -> None:
    """Saves any changes made to the dictionary back in the customer database file.

    Args:
        accounts (dict): Dictionary mapping usernames to BankAccount objects.

    Returns:
        None

    (Examples not applicable as it would wipe customer database in clients.json)
    """
    # creating an empty dictionary to add data to json file.
    data = {}

    # converting each BankAccount object back to original dictionary format.
    # key, value = username, account (just fyi).
    for username, account in accounts.items():
        data[username] = {
            "username": account.username,
            "password": account.password,
            "name": account.name,
            "account_number": account.account,
            "balance": account.balance
        }

    # copies the updated database (from accounts) back to clients.json file.
    with open('clients.json', 'w') as file:
        json.dump(data, file, indent=2)


def validate_password(password: str) -> bool:
    """Validates password meets all complexity requirements, and
        Returns true if valid. Raises ValueError otherwise.

        Password must contain:
            1. At least 6 characters
            2. At least 1 UPPERCASE character.
            3. At least 1 lowercase character.
            4. At least 1 number.
            5. At least 1 special character (!@$#% ^&*_)

    Args:
        password (str): The password user enters in order to create a new account.

    Returns:
        bool: True if password meets all requirements.
                Raises ValueError if password fails any requirement.

    Examples:
        >>> validate_password("Pass@123")
        True

        >>> validate_password("Hi@12")
        Traceback (most recent call last):
            ...
        ValueError: Password must be at least 6 characters long.

        >>> validate_password("0123456")
        Traceback (most recent call last):
            ...
        ValueError: Password must contain at least one uppercase letter.

        >>> validate_password("lower_123")
        Traceback (most recent call last):
            ...
        ValueError: Password must contain at least one uppercase letter.

        >>> validate_password("UPPER_123")
        Traceback (most recent call last):
            ...
        ValueError: Password must contain at least one lowercase letter.

        >>> validate_password("Hoo-man")
        Traceback (most recent call last):
            ...
        ValueError: Password must contain at least one number.

        >>> validate_password("BigHero6")
        Traceback (most recent call last):
            ...
        ValueError: Password must contain at least one special character (!@#$%^&*, etc.)
    """
    # initializing requirements to check.
    has_upper = False
    has_lower = False
    has_number = False
    has_special = False

    # checking minimum length:
    if len(password) < 6:
        raise ValueError("Password must be at least 6 characters long.")

    # checking each character one at a time:
    for char in password:
        if char.isupper():          # includes UPPER
            has_upper = True

        if char.islower():          # includes lower
            has_lower = True

        if char.isnumeric():        # includes number
            has_number = True

        if not char.isalnum():      # includes special character
            has_special = True

    # if requirements are not met, we raise error:
    if not has_upper:          # no UPPER char
        raise ValueError("Password must contain at least one uppercase letter.")

    if not has_special:        # no special char
        raise ValueError("Password must contain at least one special character (!@#$%^&*, etc.)")

    if not has_number:         # no number char
        raise ValueError("Password must contain at least one number.")

    if not has_lower:          # no lower char
        raise ValueError("Password must contain at least one lowercase letter.")

    return True


def generate_account_number(accounts: dict) -> str:
    """Generates the next sequential account number that represents the account.
        Finds the highest existing sequential account number in database,
        increments it by 1 and returns a new account number.

    Args:
        accounts (dict): Dictionary of BankAccount objects (from load_accounts).

    Returns:
        str: new sequential account number that follows from the most recent account number.

    Examples:
        >>> acc1 = BankAccount("ChillBill", "Bill@123", "Bill Gates", "BE001", 0)
        >>> test_accounts = {"ChillBill": acc1}
        >>> generate_account_number(test_accounts)
        'BE002'

        >>> acc2 = BankAccount("CookTim", "Tim@123", "Tim Cook", "BE002", 0)
        >>> test_accounts = {"ChillBill": acc1, "CookTim": acc2}
        >>> generate_account_number(test_accounts)
        'BE003'

        >>> acc3 = BankAccount("Adam", "Smith@123", "Adam Smith", "BE005", 0)
        >>> test_accounts = {"ChillBill": acc1, "CookTim": acc2, "Adam": acc3}
        >>> generate_account_number(test_accounts)
        'BE006'

        >>> acc4 = BankAccount("Stuart", "Little@123", "Stuart Little", "BE009", 0)
        >>> test_accounts = {"ChillBill": acc1, "CookTim": acc2, "Adam": acc3, "Stuart": acc4}
        >>> generate_account_number(test_accounts)
        'BE010'
    """
    # initializing an empty list to store existing account numbers.
    acc_numbers = []

    # iterating over each key-value pair to extract the numberic part.
    for user, account_info in accounts.items():
        account_number = account_info.account

        # indexing using len to get the numeric part -
        number_str = account_number[len(BANK_ACRONYM):]
        number_int = int(number_str)    # converting str to int.

        # adding numbers to the empty list to find maximum number in the sequence.
        acc_numbers.append(number_int)

    latest = max(acc_numbers)       # finds maximum number.
    next_number = latest + 1        # adds 1 to create the next number.

    # creates a string of account number by concatenating 'BE' with the new number.
    next_account_number = BANK_ACRONYM + str(next_number).zfill(3)
    return next_account_number


def authenticate_user(username: str, password: str, accounts: dict):
    """Checks if a username exists in file and
    authenticates access if password matches with that stored in database.

    Args:
        username (str): This is user's login id/username.
        password (str): This is user's attempted password.
        accounts (dict): This is dictionary of BankAccount objects.

    Returns:
        BankAccount or None:
        Returns the BankAccount object if the username and password matches with user's information. Else, it returns None.

    Examples:
        >>> acc1 = BankAccount("mary_j", "Spidey@123", "Mary Jane", "BE055", 12000)
        >>> accounts = {"mary_j": acc1}

        >>> login = authenticate_user("mary_j", "Spidey@123", accounts)
        >>> login is None
        False

        >>> login = authenticate_user("Octopus", "Doctor Octopus", accounts)
        >>> login is None
        True
    """
    if username in accounts:                        # checks if username exists in dictionary.
        user_account = accounts[username]           # selects the object key (username)
        if user_account.password == password:       # checks if the password matches.
            return user_account                     # grants access to user's account.
        else:
            return None         # password does not match.
    else:
        return None             # username does not exist in Dictionary.


def create_new_account(username: str, password: str, name: str, accounts: dict) -> bool:
    """Creates a new bank account for the new client.
    If the user does not already exist in database(username),
    then it calls validate_password function, generate_account_number
    and uses this to create a new BankAccount object.

    Args:
        username (str): desired unique username.
        password (str): password that must meet certain requirements.
        name (str): full name of account holder.
        accounts (dict): Dictionary of existing BankAccount objects.

    Returns:
        bool: True if account created successfully, False otherwise.

    Examples:
    #1 Trying to create new account with existing username.
    #2 Trying to create new account with new username but weak password.
        >>> test_acc = BankAccount("existing", "Pass@1", "Existing User", "BE001", 0)
        >>> test_accounts = {"existing": test_acc}

        >>> create_new_account("existing", "NewPass@123", "New User", test_accounts)
        False
        >>> create_new_account("newuser", "weak_password", "New User", test_accounts)
        False
        >>> "newuser" not in test_accounts
        True
    """
    # checking if username exists in the dictionary already.
    if username in accounts:
        return False

    # if it doesn't exist, validating if password meets requirements.
    try:
        validate_password(password)     # calling function.
    except ValueError:
        return False

    account_number = generate_account_number(accounts)      # calling function.
    new_account = BankAccount(username, password, name, account_number, NEW_ACCOUNT_BALANCE)

    # add new account to our database dictionary
    accounts[username] = new_account

    # save all changes/updates to database file.
    save_accounts(accounts)

    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)