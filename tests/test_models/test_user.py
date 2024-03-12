#!/usr/bin/python3
"""
Contains the tests for base_model module.
"""

import datetime
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test class to test different things in the User class.
    """

    def test_class_attributes(self):
        """ Tests related to class attributes """

        self.assertEqual(User.email, "")
        self.assertTrue(isinstance(User.email, str))
        self.assertTrue(isinstance(User.password, str))
        self.assertTrue(isinstance(User.first_name, str))
        self.assertTrue(isinstance(User.last_name, str))
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")
        User.first_name = "akram hany"
        User.last_name = "Sallam"
        self.assertEqual(User.first_name, "akram hany")
        self.assertEqual(User.last_name, "Sallam")
