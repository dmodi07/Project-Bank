# jobs.py
import json
from bank_account import BankAccount


def load_accounts():
    "Loads accounts from clients.json and returns dictionary of BankAccount objects"
    file_path = '/Users/dmodi07/Desktop/Learning/NEU/5001/Projects/finalproject-dmodi07/src/clients.json'
    try:
        with open(file_path, 'r') as file:
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
    try:
        




if __name__ == "__main__":
    accounts = load_accounts()
    print(f"Loaded {len(accounts)} accounts")
    
    # Test one account
    gru = accounts["grufru"]
    print(f"Name: {gru.name}")


