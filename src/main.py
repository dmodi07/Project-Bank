# main.py
from jobs import (
    BankAccount,
    load_accounts, 
    save_accounts, 
    authenticate_user, 
    create_new_account,
    validate_password
)
# CONSTANTS:
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
|  Account Holder: {name:<42}             |
|  Account Number: {account:<42}          |
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
def login(accounts):
    "Lets customers access their accounts with the Bank of Evil."
    print("\n" + "=" * 32)
    print("LOGIN TO YOUR ACCOUNT".center(32))
    print("=" * 32)

    try:
        username = input("\nUsername: ").strip()
        password = input("Password: ").strip()

        if not username or not password:
            print("\n Username and password cannot be empty.")
            input("Press Enter to continue...")
            return None
        
        user_account = authenticate_user(username, password, accounts)

        if user_account:
            print("Login Successful!")
            print(f"Welcome back, {user_account.name}!")
            input("Press Enter to continue...")
            return user_account
        else:
            print("\n Invalid username or password.")
            input("Press Enter to continue...")
            return None
    except KeyboardInterrupt:
        print("\n\n Login cancelled.")
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
        password = input("Choose Password: ").strip()
            
        if not password:
            print("\n Password cannot be empty.")
            attempts += 1

        try:
            validate_password(password)

        except ValueError as e:
            print(f"\n {e}")
            input("Press Enter to continue...")
    
        success = create_new_account(username, password, name, accounts)

        if success:
            new_account = accounts[username]
            print(f"\n✅ Account created successfully!")
            print(f"Welcome to Bank of Evil, {name}!")
            print(f"Your account number is: {new_account.account}")
            input("Press Enter to continue...")
        else:
            print("\n❌ Failed to create account. Please try again.")
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
            print(f"Invalid input! Please enter a number (1-4).")
            input("\nPress Enter to continue...")
            continue

        if choice == 1:
            print(f"Current balance: ${user_account.check_balance():.2f}")
            input("\nPress Enter to continue...")

        elif choice == 2:
            try: 
                amount = float(input("Enter deposit amount: $"))
                user_account.deposit(amount)
                save_accounts(accounts)
                print(f"${amount} deposited! Current balance: ${user_account.check_balance():.2f}")
            except (ValueError, TypeError) as e:
                print(f"Error: {e}. Please try again.")
            finally:
                input("\nPress Enter to continue...")
    
        elif choice == 3:
            try:
                amount = float(input("Enter your withdrawal amount: $"))
                user_account.withdraw(amount)
                save_accounts(accounts)
                print(f"${amount} withdrawn. Remaining balance: ${user_account.check_balance():.2f}")
            except (ValueError, TypeError) as e:
                print(f"Error: {e}. Please try again.")
            finally:
                input("\nPress Enter to continue...")
    
        elif choice == 4:
            print("Thank you for banking with us!")
            print("Logging out... \n")
            input("\nPress Enter to continue...")
            break

        else:
            print("Invalid choice. Please enter a number between [1] and [4].")
            input("\nPress Enter to continue...")


def main():
    "This is the main program file"
    try:
        try:
            accounts = load_accounts()
            print(f"\n Proudly boasting {len(accounts)} mega villains as our loyal clients!")
        except FileNotFoundError:
            print("Database file not found. Creating new database.")
            accounts = {}
        except Exception as e:
            print(f"Error loading database: {e}. Please try again.")
            print("Starting with empty database.")
            accounts = {}
    
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
                    print("\n Invalid choice! Please enter (1-3).")
                    input("Press Enter to continue...")
            
            except KeyboardInterrupt:
                print("\n\nOperation cancelled. Returning to main menu...")
                input("Press Enter to continue...")
                continue

    except KeyboardInterrupt:
        print("\n\n" + GOODBYE_MESSAGE)



if __name__ == '__main__':
    main()