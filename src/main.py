"""
Main Program file to run the Application
===========================
Course:   CS 5001
Student:  Dipen Modi

This file contains the main program to run the Bank of Evil Application.
"""

from jobs import (
    load_accounts, 
    save_accounts, 
    authenticate_user, 
    create_new_account,
    validate_password
)

# CONSTANTS:
MAX_LOGIN_ATTEMPTS = 3
MAIN_MENU = """
+=========================================+
|                                         |
|             BANK OF EVIL                |
|      Financing Villainy Since 2010      |
|                                         |
+=========================================+
|                                         |
|          MAIN MENU                      |
|                                         |
|      [1] Login to Account               |
|      [2] Create New Account             |
|      [3] Exit                           |
|                                         |
+=========================================+
"""

BANKING_MENU_TEMPLATE = """
+=========================================+
|         BANK OF EVIL                    |
|       BANKING SERVICES                  |
+=========================================+
   Account Holder: {name:<23}
   Account Number: {account:<23}
+-----------------------------------------+
|                                         |
|  [1] Check Balance                      |
|  [2] Deposit Money                      |
|  [3] Withdraw Money                     |
|  [4] Logout                             |
|                                         |
+=========================================+
"""

EXIT_MESSAGE = """
+=================================================+
|                                                 |
|    Thank you for banking with BANK OF EVIL!     |
|                  See you soon!                  |
|                                                 |
+=================================================+
"""


# verifying login details -
def login(accounts: dict):
    """Lets customers access their accounts with the Bank of Evil.
    Interactive menu for users to insert their username and password
    in order to login to their respective account. Validates them.
    In case of 3 incorrect attempts, returns the Main Menu.

    Args:
        accounts (dict): Dictionary of BankAccount objects loaded from database.

    Returns:
        BankAccount or None: Returns authenticated BankAccount object if successful. None, if the authentication fails.

    (Doctest examples not possible as this function is interactive and requires user input. Function has been manually tested. See documentation for test screenshots).
    """
    # adding visuals for header -
    print("\n" + "=" * 32)
    print("LOGIN TO YOUR ACCOUNT".center(32))
    print("=" * 32)

    # to allow users to retry upto 3 times (MAX_LOGIN_ATTEMPTS) in case of authentication failure.
    for attempt in range(MAX_LOGIN_ATTEMPTS):
        try:
            # getting credentials from user.
            username = input("Username: ").strip()
            password = input("Password: ").strip()

            # in case of no input by user -
            if not username or not password:
                print("\n Username and password cannot be empty.")
                remaining = MAX_LOGIN_ATTEMPTS - attempt - 1        # only 3 tries allowed each time so keeping track of attempts.
                if remaining > 0:
                    print(f"Attempts remaining: {remaining}")
                    continue
                else:
                    print("Maximum login attempts reached! Returning to Main Menu.")
                    input("Press Enter to continue...")
                    return None
            
            # once the username and password is inserted, checking if it matches with that in our database -
            user_account = authenticate_user(username, password, accounts)

            if user_account:        # in case of match, allowing account access.
                print("\nLogin Successful!")
                print(f"Welcome back, {user_account.name}!")
                input("Press Enter to continue...")
                return user_account

            # if no match found, return error message and track attempt.
            else:
                remaining = MAX_LOGIN_ATTEMPTS - attempt - 1
                if remaining > 0:
                    print("\n Invalid username or password.")
                    print(f"Attempts remaining: {remaining}")
                    input("Press Enter to continue...")

                else:       # return to Main Menu if no more attempts left.
                    print("\n Invalid username or password.")
                    print("Maximum login attempts reached. Returning to Main Menu.")
                    input("Press Enter to continue...")
                    return None

        except Exception as e:
            print(f"\n Unexpected error during login: {e}")
            input("Press Enter to continue...")
            return None


def create_account(accounts):
    "Creates new account if the user does not have an account with Bank of Evil."
    print("\n" + "=" * 32)
    print("CREATE NEW ACCOUNT".center(32))
    print("=" * 32)

    try:
        # name part
        name = input("\n Full Name: ").strip()
        if not name:
            print("\n Name cannot be empty.")
            input("Press Enter to continue...")
            return
        
        # username part
        username = input("Choose Username: ").strip()
        if not username:
            print("\n Username cannot be empty.")
            input("Press Enter to continue...")
            return

        if username in accounts:
            print(f"\n Username '{username} is already taken. Try again!")
            input("Press Enter to continue...")
            return

        # password part
        while True:
            password = input("Choose Password: ").strip()

            if not password:
                print("\n Password cannot be empty. Please try again!\n")
                continue

            try:
                validate_password(password)
                break

            except ValueError as e:
                print(f"\n {e}")
                print("Please try again.\n")
    
        # finally creating account since everything is valid.    
        success = create_new_account(username, password, name, accounts)

        if success:
            new_account = accounts[username]
            print(f"\n Account created successfully!")
            print(f"Welcome to The Bank of Evil, {name}!")
            print(f"Your account number is: {new_account.account}")
            input("Press Enter to continue...")

        else:
            print("\n Failed to create account. Please try again.")
            input("Press Enter to continue...")

    except KeyboardInterrupt:
        print("\n\n Account creation cancelled.")
        input("Press Enter to continue...")

    except Exception as e:
        print(f"\n Unexpected error: {e}")
        input("Press Enter to continue...")


def banking_menu(user_account, accounts):
    while True:
        print(BANKING_MENU_TEMPLATE.format(
            name = user_account.name,
            account = user_account.account
        ))

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("\nInvalid input! Please enter a number (1-4).")
            input("Press Enter to continue...")
            continue

        if choice == 1:     # checks balance in account.
            print(f"Current balance: ${user_account.check_balance():.2f}")
            input("\nPress Enter to continue...")

        elif choice == 2:   # deposits money to account.
            try: 
                amount = float(input("Enter deposit amount: $"))
                user_account.deposit(amount)
                save_accounts(accounts)
                print(f"\n${amount:,.2f} deposited successfully! Current balance: ${user_account.check_balance():.2f}")

            except (ValueError, TypeError) as e:
                print(f"\nError: {e}. Please try again.")

            finally:
                input("Press Enter to continue...")
    
        elif choice == 3:   # withdraw money from account.
            try:
                amount = float(input("\nEnter your withdrawal amount: $"))
                user_account.withdraw(amount)
                save_accounts(accounts)
                print(f"\n ${amount:,.2f} withdrawn successfully. Remaining balance: ${user_account.check_balance():.2f}")

            except (ValueError, TypeError) as e:
                print(f"\nError: {e}. Please try again.")

            finally:
                input("Press Enter to continue...")
    
        elif choice == 4:   # Exiting the program/logging out of account.
            print("\n Thank you for banking with us!")
            print("Logging out... \n")
            input("Press Enter to continue...")
            break

        else:
            print("\n Invalid choice. Please enter a number between [1] and [4].")
            input("Press Enter to continue...")


def main():
    "This is the main program file"
    try:        # load accounts from database (clients.json)
        try:
            accounts = load_accounts()
            print(f"\nProudly boasting {len(accounts)} mega villains as our loyal clients!")
        except FileNotFoundError:
            print("\nDatabase file not found. Creating new database.")
            accounts = {}
        except Exception as e:
            print(f"Error loading database: {e}. Please try again.")
            print("Starting with empty database.")
            accounts = {}

        # Main Menu loop as the Homepage of my program.
        while True:
            try:
                print(MAIN_MENU)
                choice = input("Please select an option (1-3): ").strip()

                if choice == "1":
                    user_account = login(accounts)
                    if user_account:
                        banking_menu(user_account, accounts)
                
                elif choice == "2":
                    create_account(accounts)
                
                elif choice == "3":
                    print(EXIT_MESSAGE)
                    break

                else:
                    print("\nInvalid choice! Please enter (1-3).")
                    input("Press Enter to continue...")
            
            except KeyboardInterrupt:
                print("\n\nOperation cancelled. Returning to main menu...")
                input("Press Enter to continue...")
                continue

    except KeyboardInterrupt:
        print("\n\n" + EXIT_MESSAGE)


if __name__ == "__main__":
    main()

    