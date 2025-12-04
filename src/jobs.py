# jobs.py
import json
from bank_account import BankAccount


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


if __name__ == "__main__":
    accounts = load_accounts()
    print(f"Loaded {len(accounts)} accounts")
    
    # Test one account
    gru = accounts["grufru"]
    print(f"Gru's balance before: ${gru.balance}")
    gru.withdraw(20000)
    print(f"Gru's balance after: ${gru.balance}")
    
    # Save the changes
    save_accounts(accounts)
    print("Saved changes to clients.json")
    
    # Load again to verify it was saved
    accounts2 = load_accounts()
    gru2 = accounts2["grufru"]
    print(f"Gru's balance after reloading: ${gru2.balance}")

    # password check:
    while True:
        password = input("Please enter a password:")
        if validate_password(password) == True:
            break


