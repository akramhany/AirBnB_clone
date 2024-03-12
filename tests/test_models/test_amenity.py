#!/usr/bin/python3
"""
Contains the tests for amenity module.
"""

import datetime
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test class to test different things in the Amenity class.
    """

    def test_class_attributes(self):
        """ Tests related to class attributes """

        self.assertEqual(Amenity.name, "")
        self.assertTrue(isinstance(Amenity.name, str))
        Amenity.name = "Cairo"
        self.assertEqual(Amenity.name, "Cairo")
