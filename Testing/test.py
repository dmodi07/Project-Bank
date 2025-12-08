"""
Unit Tests for the Application
===========================
Course:   CS 5001
Student:  Dipen Modi

This file contains unittests for all functions.
"""
import sys
import os

# Add the src folder to Python's path
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
import unittest
from bank_account import BankAccount

class Test_BankAccount(unittest.TestCase):

    # create fresh test accounts here.
    def setUp(self):
        """Runs before each test method so that each test gets a clean acocunt to work with.

        Args:
            unittest (_type_): _description_
        """
        # creating an account with zero balance.
        self.empty_account = BankAccount(
            "testuser1",
            "testpass",
            "Test User",
            "TEST001",
            0.0
        )

        # creating an account with some money
        self.funded_account = BankAccount(
            "testuser2",
            "testpass2",
            "Rich User",
            "TEST002",
            1000.0
        )

    def test_something(self):
        """Each test method tests ONE specific thing."""
        pass

    # clean up if needed
    def tearDown(self):
        """Runs AFTER each test method."""
        pass

if __name__ == "__main__":
    unittest.main()
