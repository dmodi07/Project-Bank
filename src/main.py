# main.py
from jobs import BankAccount


def operations():
    gru_account = BankAccount("Mr. Gru", "AC101", 1000)
    nefario_account = BankAccount("Dr. Nefario", "AC002", 500)


    try:
        gru_account.deposit("sd")
        print(f"Deposit successful! Balance: ${gru_account.check_balance():.2f}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

    try:
        gru_account.deposit(500)
        print(f"Deposit successful! Balance: ${gru_account.check_balance():.2f}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

    try:
        gru_account.withdraw(2000)
        print(f"Withdrawal successful. New balance: ${gru_account.check_balance():.2f}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

    try:
        gru_account.withdraw(50)
        print(f"Withdrawal successful. New balance: ${gru_account.check_balance():.2f}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

    try:
        gru_account.withdraw(1000)
        print(f"Withdrawal successful. New balance: ${gru_account.check_balance():.2f}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

    print(f"\nFinal balance: ${gru_account.check_balance():.2f}")

def main():
    print("Welcome to the Bank of Evil!")
    operations()



if __name__ == '__main__':
    main()