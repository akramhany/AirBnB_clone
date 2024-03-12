#!/usr/bin/python3
"""
Contains the tests for review module.
"""

import datetime
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test class to test different things in the Review class.
    """

    def test_class_attributes(self):
        """ Tests related to class attributes """

        self.assertEqual(Review.place_id, "")
        self.assertTrue(isinstance(Review.place_id, str))
        Review.place_id = "123-123-123"
        self.assertEqual(Review.place_id, "123-123-123")
    
    def test_class_attributes(self):
        """ Tests related to class attributes """

        self.assertEqual(Review.user_id, "")
        self.assertTrue(isinstance(Review.user_id, str))
        Review.user_id = "123-123-123"
        self.assertEqual(Review.user_id, "123-123-123")
    
    def test_class_attributes(self):
        """ Tests related to class attributes """

        self.assertEqual(Review.text, "")
        self.assertTrue(isinstance(Review.text, str))
        Review.user = "blabla"
        self.assertEqual(Review.user, "blabla")
