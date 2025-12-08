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
|               See you next time!                |
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
        # getting credentials from user.
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        # in case of no input by user -
        if not username or not password:
            print("\nUsername and password cannot be empty.")
            remaining = MAX_LOGIN_ATTEMPTS - attempt - 1        # only 3 tries allowed each time so keeping track of attempts.

            if remaining > 0:
                print(f"Attempts remaining: {remaining}")
                input("Press Enter to continue...")
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
                print("\nInvalid username or password.")
                print(f"Attempts remaining: {remaining}")
                input("Press Enter to continue...")

            else:       # return to Main Menu if no more attempts left.
                print("\nInvalid username or password.")
                print("Maximum login attempts reached. Returning to Main Menu.")
                input("Press Enter to continue...")
                return None

    return None


def create_account(accounts: dict) -> None:
    """Creates new account if the user does not have an account with Bank of Evil.
    Interactive Menu that guides users through account creation, by asking for desired username and password, whilst also doing validation by calling validate_password function. Keeps asking until valid password is provided or user cancels.

    Args:
        accounts (dict): Dictionary of BankAccount objects.

    Returns:
        None

    (Doctest examples not possible as this function is interactive and requires user input. Function has been manually tested. See documentation for test screenshots).
    """
    # adding visuals for header -
    print("\n" + "=" * 38)
    print("CREATE NEW ACCOUNT".center(38))
    print("=" * 38)

    try:
        # name part
        name = input("Full Name: ").strip()
        if not name:
            print("\nName cannot be empty.")
            input("Press Enter to continue...")
            return

        # username part
        username = input("Choose Username: ").strip()
        if not username:
            print("\nUsername cannot be empty.")
            input("Press Enter to continue...")
            return

        if username in accounts:
            print(f"\nUsername '{username} is already taken. Try again!")
            input("Press Enter to continue...")
            return

        # password part
        while True:
            password = input("Choose Password: ").strip()

            if not password:
                print("\nPassword cannot be empty. Please try again!\n")
                continue

            try:   # this is where it checks whether password is meets requirements or not.
                validate_password(password)     # simply calling function for this.
                break

            except ValueError as e:
                print(f"\n{e}")
                print("Please try again.\n")

        # finally creating account since everything is valid by calling function create_new_account.
        create_new_account(username, password, name, accounts)

        # retrieving information of this new account to display message for feedback to user -
        new_account = accounts[username]
        print(f"Account created successfully!\n")
        print(f"Welcome to The Bank of Evil, {name}!")
        print(f"Your account number is: {new_account.account}")
        print("Please sign in to access our services.")
        print("-" * 38)
        input("Press Enter to continue...")

    except Exception as e:
        print(f"\n Unexpected error: {e}")
        input("Press Enter to continue...")


def banking_menu(user_account, accounts: dict) -> None:
    """Display banking operations menu for authenticated user.
    Provides interface for checking balance, depositing money, withdrawing money and logging out. All transactions made get saved to clients.json database file. This interface continues until user chooses to log out.

    Args:
        user_account (Bank_Account): This is the authenticated user's BankAccount object only.
        accounts (dict): Dictionary of all BankAccount objects. This is to save any update in database file.

    (Doctest examples not provided as function requires interactive user input and modifies database state. Function has been manually tested.)
    """
    # looping banking operations interface using template to look neat -
    while True:
        # fills username and account number in the template itself for user experience.
        print(BANKING_MENU_TEMPLATE.format(
            name=user_account.name,
            account=user_account.account
        ))

        try:
            # asking customer to choose what they want to do.
            choice = int(input("Enter your choice (1-4): "))

        except ValueError:
            print("\nInvalid input! Please enter a number (1-4).")
            input("Press Enter to continue...")
            continue

        if choice == 1:     # checks balance in account.
            print("-" * 43)
            print(f"Current balance: ${user_account.check_balance():.2f}")
            input("Press Enter to continue...")


        elif choice == 2:   # deposits money to account.
            try:
                print("-" * 43)
                amount = float(input("Enter deposit amount: $"))
                user_account.deposit(amount)    # calling deposit method from BankAccount class.
                save_accounts(accounts)         # saving transaction to database.
                print(f"\n${amount:,.2f} deposited successfully!\nCurrent balance: ${user_account.check_balance():.2f}")
                print("-" * 43)

            except (ValueError, TypeError) as e:
                print(f"\nError: {e}. Please try again.")

            finally:
                input("Press Enter to continue...\n")

        elif choice == 3:   # withdraw money from account.
            try:
                print("-" * 43)
                amount = float(input("Enter your withdrawal amount: $"))
                user_account.withdraw(amount)    # calling withdraw method from BankAccount class.
                save_accounts(accounts)          # saving transaction to database.
                print(f"\n${amount:,.2f} withdrawn successfully.\nRemaining balance: ${user_account.check_balance():.2f}")
                print("-" * 43)

            except (ValueError, TypeError) as e:
                print(f"\nInvalid entry! Please try again.")

            finally:
                input("Press Enter to continue...")

        elif choice == 4:   # Exiting the program/logging out of account.
            print("\nThank you for banking with us!")
            print("Logging out...")
            print("-" * 43)
            input("Press Enter to continue...")
            break

        else:
            print("\nInvalid choice. Please enter a number between [1] and [4].")
            input("Press Enter to continue...")


def main() -> None:
    """This is the main program file.
        Loads the database and displays the Main Menu. Calls other functions as per user's choice (for example, login, create new account or exit.) The Main Menu is in a loop that continues to display the interface until user chooses to Exit from the application.

        Args:
            None

        Returns:
            None

        (Doctest examples not provided as function requires interactive user input
        and manages entire application lifecycle. Function has been manually tested).
    """
    # load accounts from database (clients.json) to begin.
    accounts = load_accounts()
    print(f"\nProudly boasting {len(accounts)} mega villains as our loyal clients!")

    # continues Main Menu loop as the Homepage of my program.
    while True:
        print(MAIN_MENU)
        choice = input("Please select an option (1-3): ").strip()

        # if user has an account, and wants to login -
        if choice == "1":
            user_account = login(accounts)
            if user_account:                                # if user_account exists, then -
                banking_menu(user_account, accounts)        # calls banking_menu function for making transactions.

        # if user does not have an account, but wants to make one -
        elif choice == "2":
            create_account(accounts)     # calls create_account function to make new account.

        # if user chooses to exit -
        elif choice == "3":
            print(EXIT_MESSAGE)
            break

        else:
            print("\nInvalid choice! Please enter (1-3).")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
