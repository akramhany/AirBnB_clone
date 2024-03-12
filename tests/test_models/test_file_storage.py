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

    def test_class_attributes(self):
        """ Test the class attributes of the FileStorage class """

        with self.assertRaises(AttributeError):
            print(FileStorage.__file_path)

        with self.assertRaises(AttributeError):
            print(FileStorage.__objects)

        b1 = BaseModel()
        updated_at = b1.updated_at
        b1.save()
        self.assertNotEqual(b1.updated_at, updated_at)

    def test_general(self):
        """ General Tests """

        storage = FileStorage()

        b1 = BaseModel()

        self.assertTrue(isinstance(storage.all(), dict))
        storage.new(b1)
        self.assertTrue(b1 in storage.all().values())
