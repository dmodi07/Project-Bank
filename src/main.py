# main.py
from jobs import BankAccount


def operations():
    john_account = BankAccount("John Smith", "AC101", 1000)
    sarah_account = BankAccount("Sarah Connor", "AC002", 500)

    try:
        john_account.deposit("sd")
        print(f"Deposit successful! Balance: ${john_account.check_balance():.2f}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

    try:
        john_account.deposit(500)
        print(f"Deposit successful! Balance: ${john_account.check_balance():.2f}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

    try:
        john_account.withdraw(2000)
        print(f"Withdrawal successful. New balance: ${john_account.check_balance():.2f}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

    try:
        john_account.withdraw(50)
        print(f"Withdrawal successful. New balance: ${john_account.check_balance():.2f}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

    try:
        john_account.withdraw(1000)
        print(f"Withdrawal successful. New balance: ${john_account.check_balance():.2f}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

    print(f"\nFinal balance: ${john_account.check_balance():.2f}")

def main():
    pass



if __name__ == '__main__':
    main()