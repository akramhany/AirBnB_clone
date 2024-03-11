#!/usr/bin/python3
"""
Contains the tests for file_storage module.
"""

import datetime
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Test class to test different things in the BaseModel class.
    """

    def test_general(self):
        """ General Tests """

        storage = FileStorage()
        b1 = BaseModel()

        self.assertTrue(isinstance(storage.all(), dict))
        storage.new(b1)
        self.assertTrue(b1 in storage.all().values())
