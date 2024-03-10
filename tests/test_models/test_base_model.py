#!/usr/bin/python3
"""
Contains the tests for base_model module.
"""

import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test class to test different things in the BaseModel class.
    """

    def test_id(self):
        """ Tests related to id """

        b1 = BaseModel()
        b2 = BaseModel()

        self.assertNotEqual(b1.id, b2.id)
        self.assertTrue(isinstance(b1.id, str))

    def test_general(self):
        """ Test general things """

        b1 = BaseModel()

        b1_dict = b1.to_dict()
        self.assertTrue(isinstance(b1_dict, dict))
        self.assertTrue(isinstance(b1.created_at, datetime.datetime))
        self.assertTrue(isinstance(b1.updated_at, datetime.datetime))
        self.assertEqual(b1_dict["__class__"], "BaseModel")
        self.assertTrue(isinstance(b1_dict["created_at"], str))
