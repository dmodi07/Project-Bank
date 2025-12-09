"""
Unit Tests for the Application
===========================
Course:   CS 5001
Student:  Dipen Modi

This file contains unittests for all functions.
"""
import sys
import os
import unittest
from bank_account import BankAccount
from jobs import (
                validate_password,
                generate_account_number,
                authenticate_user)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
# Add the src folder to Python's path
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestBankAccount(unittest.TestCase):

    # creating an object with zero balance.
    def setUp(self):
        """Tests that BankAccount initializes correctly."""
        self.goblin = BankAccount(
            "MrScientist",
            "Green_Goblin@95",
            "Norman Osborn",
            "BE015",
            0.0
        )
        # creating an object with some money.
        self.jean_bean = BankAccount(
            "jeandbean",
            "C1aw_&_0rder!",
            "Jean Clawed",
            "BE010",
            15000.0
        )
        # extra test (just testing).
        self.knuckles = BankAccount(
            "knuckles",
            "Veg@sHeist_#12",
            "Wild Knuckles",
            "BE011",
            180000.0
        )

    def test_init_goblin(self):
        """Tests that BankAccount initializes correctly for Green Goblin"""
        self.assertEqual(self.goblin.username, "MrScientist")
        self.assertEqual(self.goblin.password, "Green_Goblin@95")
        self.assertEqual(self.goblin.name, "Norman Osborn")
        self.assertEqual(self.goblin.account, "BE015")
        self.assertEqual(self.goblin.balance, 0.0)

    def test_init_jean(self):
        """Tests that BankAccount initializes correctly for Jean Clawed"""
        self.assertEqual(self.jean_bean.username, "jeandbean")
        self.assertEqual(self.jean_bean.password, "C1aw_&_0rder!")
        self.assertEqual(self.jean_bean.name, "Jean Clawed")
        self.assertEqual(self.jean_bean.account, "BE010")
        self.assertEqual(self.jean_bean.balance, 15000.0)

    def test_deposit(self):
        """Tests that a deposit is made successfully to user's account"""
        self.goblin.deposit(100)
        self.assertEqual(self.goblin.balance, 100)

        self.jean_bean.deposit(5000)
        self.assertEqual(self.jean_bean.balance, 20000)

    def test_withdrawal(self):
        """Tests that a withdrawal is made successfully from account"""
        self.knuckles.withdraw(29999.99)
        self.assertAlmostEqual(self.knuckles.balance, 150000.01)

        self.knuckles.withdraw(0.01)
        self.assertAlmostEqual(self.knuckles.balance, 150000)

    def test_withdraw_none_raises_error(self):
        """Test that withdrawing None raises TypeError."""
        with self.assertRaises(TypeError):
            self.knuckles.withdraw(None)

    def test_deposit_none_raises_error(self):
        """Test that depositing nothing raises TypeError."""
        with self.assertRaises(TypeError):
            self.knuckles.deposit(None)


class TestValidatePassword(unittest.TestCase):
    """Tests the validate_password function to see if it correct."""

    def test_valid_password(self):
        """Tests whether the password is valid or not"""
        self.assertTrue(validate_password("Pass@123!"))
        self.assertTrue(validate_password("Jim-Jam-12"))

    def test_no_lower(self):
        """Tests that the password raises value error if no lowercase letter in it"""
        with self.assertRaises(ValueError):
            validate_password("UPPER@123")

    def test_no_upper(self):
        """Tests that the password raises value error if there's no uppercase letter"""
        with self.assertRaises(ValueError):
            validate_password("lower@123")

    def test_no_special(self):
        """Tests that the password raises value error if there is no special character """
        with self.assertRaises(ValueError):
            validate_password("NoSpecia1")

    def test_no_special(self):
        """Tests that the password raises value error if there are less than 6 characters in the password."""
        with self.assertRaises(ValueError):
            validate_password("Not_6")

    def test_no_special(self):
        """Tests that the password raises value error if there is no number in it"""
        with self.assertRaises(ValueError):
            validate_password("No_Number")


class TestGenerateAccount(unittest.TestCase):
    """Tests the generate_account_number function from jobs.py"""

    def setUp(self):
        """Introducing these accounts as if they are the last account made for testing."""
        self.goblin = BankAccount(
                "MrScientist",
                "Green_Goblin@95",
                "Norman Osborn",
                "BE015",
                0.0
            )
        self.jean_bean = BankAccount(
            "jeandbean",
            "C1aw_&_0rder!",
            "Jean Clawed",
            "BE010",
            15000.0
        )

    def test_generate_account_number(self):
        # check new account (if goblin's is the last account)
        test_new_1 = {"goblin": self.goblin}
        self.assertEqual(generate_account_number(test_new_1), "BE016")

        # check another new account (if Jean's is the last account)
        test_new_2 = {"jean_bean": self.jean_bean}
        self.assertEqual(generate_account_number(test_new_2), "BE011")


class TestAuthenticateUser(unittest.TestCase):
    """Tests the Authenticate_user function in jobs.py"""

    def setUp(self):
        """Creating same tests accounts as before to authenticate user for logging into account."""
        self.goblin = BankAccount(
                "MrScientist",
                "Green_Goblin@95",
                "Norman Osborn",
                "BE015",
                0.0
            )
        self.jean_bean = BankAccount(
            "jeandbean",
            "C1aw_&_0rder!",
            "Jean Clawed",
            "BE010",
            15000.0
        )
        self.accounts = {"MrScientist": self.goblin, "jeandbean": self.jean_bean}

    def test_correct_credentials(self):
        """Tests if correct credentials are used to login to account."""
        login_goblin = authenticate_user("MrScientist", "Green_Goblin@95", self.accounts)
        self.assertIsNotNone(login_goblin)
        self.assertEqual(login_goblin.username, "MrScientist")

        login_jean = authenticate_user("jeandbean", "C1aw_&_0rder!", self.accounts)
        self.assertIsNotNone(login_jean)
        self.assertEqual(login_jean.password, "C1aw_&_0rder!")

    def test_authenticate_user_with_wrong_username(self):
        """Tests that wrong username returns None."""
        login = authenticate_user("Octopus", "Doctor Octopus", self.accounts)
        self.assertIsNone(login)


if __name__ == "__main__":
    unittest.main(verbosity=2)
