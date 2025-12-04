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
        




if __name__ == "__main__":
    accounts = load_accounts()
    print(f"Loaded {len(accounts)} accounts")
    
    # Test one account
    gru = accounts["grufru"]
    print(f"Name: {gru.name}")


