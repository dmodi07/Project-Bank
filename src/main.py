# main.py
from jobs import BankAccount

welcome_message = print("""
\nWelcome to the Bank of Evil!
============= Bank Menu =============
1. Deposit money     3. Check Balance
2. Withdraw money    4. Exit
""")

# must load database first -

# option to login to account -
username = input("Username: ")
password = input("Password: ")

# verifying login details -
user_account = authenticate_user(username, password, accounts)
if user_account:
    print(f"Login successful! Welcome {user_account.name}\n")
else:
    print("Login failed! Please try again.\n")


def main():
    account = BankAccount("johns", "JSmith@01", "John Smith", "AC001", 1000)

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



if __name__ == '__main__':
    main()