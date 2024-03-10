#!/usr/bin/python3
"""
Contains the tests for base_model module.
"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_creation_id(self):
        b1 = BaseModel()
        b2 = BaseModel()

        self.assertNotEqual(b1.id, b2.id)
        self.assertTrue(isinstance(b1.to_dict(), dict))
