#!/usr/bin/python3
"""
Contains the tests for state module.
"""

import datetime
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Test class to test different things in the State class.
    """

    def test_class_attributes(self):
        """ Tests related to class attributes """

        self.assertEqual(State.name, "")
        self.assertTrue(isinstance(State.name, str))
        State.name = "Cairo"
        self.assertEqual(State.name, "Cairo")
