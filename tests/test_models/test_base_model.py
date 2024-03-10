#!/usr/bin/python3
"""
Contains the tests for base_model module.
"""

import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_id(self):
        b1 = BaseModel()
        b2 = BaseModel()

        self.assertNotEqual(b1.id, b2.id)
        self.assertTrue(isinstance(b1.id, str))

    def test_general(self):
        b1 = BaseModel()

        self.assertTrue(isinstance(b1.to_dict(), dict))
        self.assertTrue(isinstance(b1.created_at, datetime.datetime))
        self.assertTrue(isinstance(b1.updated_at, datetime.datetime))
