#!/usr/bin/python3
"""
Contains the tests for city module.
"""

import datetime
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test class to test different things in the City class.
    """

    def test_class_attributes(self):
        """ Tests related to class attributes """

        self.assertEqual(City.name, "")
        self.assertTrue(isinstance(City.name, str))
        City.name = "Cairo"
        self.assertEqual(City.name, "Cairo")
        self.assertEqual(City.state_id, "")
        self.assertTrue(isinstance(City.state_id, str))
        City.state_id = "123-123-123"
        self.assertEqual(City.state_id, "123-123-123")
