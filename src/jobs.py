# jobs.py
import json
from bank_account import BankAccount

# constants:
BANK_ACRONYM = "BE"
NEW_ACCOUNT_BALANCE = 0.0


def load_accounts():
    "Loads accounts from clients.json and returns dictionary of BankAccount objects"
    try:
        with open('clients.json', 'r') as file:
            data = json.load(file)

        accounts = {}
        for username, info in data.items():
            account = BankAccount(
                info["username"],
                info["password"],
                info["name"],
                info["account_number"],
                info["balance"]
            )
            accounts[username] = account
        # print(type(accounts))
        return accounts
    except FileNotFoundError:
        return {}  
    

def save_accounts(accounts):
    "Saves any changes made to the dictionary back in the customer database file"
    data = {}
    for username, account in accounts.items():
        data[username] = {
            "username": account.username,
            "password": account.password,
            "name": account.name,
            "account_number": account.account,
            "balance": account.balance
        }
    
    with open('clients.json', 'w') as file:
        json.dump(data, file, indent = 2)
        

def validate_password(password):
    """Validates password meets complexity requirements
        Returns true if valid, raises ValueError if not."""
    
    has_upper = False
    has_lower = False
    has_number = False
    has_special = False

    if len(password) < 6:
        raise ValueError("Password must be at least 6 characters long.")

    for char in password:
        if char.isupper():
            has_upper = True

        if char.islower():
            has_lower = True          

        if char.isnumeric():
            has_number = True 
        
        if not char.isalnum():
            has_special = True

    if not has_upper:
        raise ValueError("Password must contain at least one uppercase letter.")

    if not has_special:
        raise ValueError("Password must contain at least one special character (!@#$%^&*, etc.)")

    if not has_number:    
        raise ValueError("Password must contain at least one number.")
    
    if not has_lower:
        raise ValueError("Password must contain at least one lowercase letter.")

    return True


def generate_account_number(accounts):
    """Generates the next sequential account number that represents the account.

    Args:
        accounts (dict): Dictionary of BankAccount objects (from load_accounts).

    Returns:
        new sequential account number that follows from the most recent account number.
    """
    acc_numbers = []

    for user, account_info in accounts.items():
        account_number = account_info.account
        number_str = account_number[len(BANK_ACRONYM):]
        number_int = int(number_str)
        acc_numbers.append(number_int)
    
    latest = max(acc_numbers)
    next_number = latest + 1
    next_account_number = BANK_ACRONYM + str(next_number).zfill(3)
    return next_account_number


def authenticate_user(username: str, password: str, accounts: dict):
    """Checks if a username exists in file and authenticates access if password matches.

    Args:
        username (str): This is user's login id/username
        password (str): This is their password
        accounts (dict): This is dictionary of BankAccount objects.
    
    Returns: 
        BankAccount (If the username and password matches with user's information then it returns the BankAccount object. Else, it returns None.)
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

    Args:
        username (str): desired unique username.
        password (str): password that must certain requirements.
        name (str): full name of account holder.
        accounts (dict): Dictionary of existing BankAccount objects.

    Returns:
        bool: True if account created successfully, False otherwise.
    """
    # checking if username exists in the dictionary already.
    if username in accounts:
        return False
    
    # if it doesn't exist, validating if password meets requirements.
    try:
        validate_password(password)  
    except ValueError: 
        return False
    
    account_number = generate_account_number(accounts)
    new_account = BankAccount(username, password, name, account_number, NEW_ACCOUNT_BALANCE)

    # add new account to dictionary
    accounts[username] = new_account

    # save new account to database
    save_accounts(accounts)

    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
