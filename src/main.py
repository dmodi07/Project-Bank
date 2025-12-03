# main.py
from jobs import BankAccount
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

welcome_message = print("""
\nWelcome to the Bank of Evil!
============= Bank Menu =============
1. Deposit money     3. Check Balance
2. Withdraw money    4. Exit
""")

def operations():
    gru_account = BankAccount("Felonious Gru", "BE001", 250000)
    nefario_account = BankAccount("Joseph Nefario", "BE002", 45000)
    stuart_account = BankAccount("Stuart D'Minion", "BE003", 9)
    dave_account = BankAccount("Dave D'Minion", "BE004", 8)
    bob_account = BankAccount("Bob D'Minion", "BE005", 7)
    vector_account = BankAccount("Vector Perkins", "BE006", 850000)
    macho_account = BankAccount("El Macho", "BE007", 400000)
    scarlet_account = BankAccount("Scarlet Overkill", "BE008", 750000)
    max_account = BankAccount("Maxime Le Mal", "BE009", 300000)
    jean_account = BankAccount("Jean Clawed", "BE010", 15000)
    knuckles_account = BankAccount("Wild Knuckles", "BE011", 180000)
    eduardo_account = BankAccount("Eduardo Perez", "BE012", 120000)

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
    account = BankAccount("John Smith", "AC001", 1000)

    while True:
        print(welcome_message)

        try:
            choice = int(input("Enter your choice (1-4): "))
        except TypeError:
            print(f"Invalid input! Please enter a number.")

        if choice == 1:
            try: 
                amount = float(input("Enter deposit amount: $"))
                account.deposit(amount)
                print(f"${amount} deposited! Current balance: ${account.check_balance():.2f}")
            except (ValueError, TypeError) as e:
                print(f"Error: {e}. Please try again.")

        elif choice == 2:
            try:
                amount = float(input("Enter your withdrawal amount: $"))
                account.withdraw(amount)
                print(f"${amount} withdrawn. Remaining balance: ${account.check_balance():.2f}")
            except (ValueError, TypeError) as e:
                print(f"Error: {e}. Please try again.")

        elif choice == 3:
            print(f"Current balance: ${account.check_balance():.2f}")

        elif choice == 4:
            print("Thank you for banking with us!")
            break

        else:
            print("Invalid choice. Please try again.")
    operations()


if __name__ == '__main__':
    main()