#!/usr/bin/python3
"""
Contains the tests for place module.
"""

import datetime
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test class to test different things in the Place class.
    """

    def test_class_attributes_city_id(self):
        """ Tests related to class attributes """

        self.assertEqual(Place.city_id, "")
        self.assertTrue(isinstance(Place.city_id, str))
        Place.city_id = "123-123-123"
        self.assertEqual(Place.city_id, "123-123-123")

    def test_class_attributes_user_id(self):
        """ Tests related to class attributes """

        self.assertEqual(Place.user_id, "")
        self.assertTrue(isinstance(Place.user_id, str))
        Place.user_id = "123-123-123"
        self.assertEqual(Place.user_id, "123-123-123")

    def test_class_attributes_name(self):
        """ Tests related to class attributes """

        self.assertEqual(Place.name, "")
        self.assertTrue(isinstance(Place.name, str))
        Place.name = "sharqya"
        self.assertEqual(Place.name, "sharqya")

    def test_class_attributes_description(self):
        """ Tests related to class attributes """

        self.assertEqual(Place.description, "")
        self.assertTrue(isinstance(Place.description, str))
        Place.description = "its a wonderful place"
        self.assertEqual(Place.description, "its a wonderful place")

    def test_class_attributes_number_rooms(self):
        """ Tests related to class attributes """

        self.assertEqual(Place.number_rooms, 0)
        self.assertTrue(isinstance(Place.number_rooms, int))
        Place.number_rooms = 5
        self.assertEqual(Place.number_rooms, 5)

    def test_class_attributes_number_bathrooms(self):
        """ Tests related to class attributes """

        self.assertEqual(Place.number_bathrooms, 0)
        self.assertTrue(isinstance(Place.number_bathrooms, int))
        Place.number_bathrooms = 5
        self.assertEqual(Place.number_bathrooms, 5)
    
    def test_class_attributes_max_guest(self):
        """ Tests related to class attributes """

        self.assertEqual(Place.max_guest, 0)
        self.assertTrue(isinstance(Place.max_guest, int))
        Place.max_guest = 5
        self.assertEqual(Place.max_guest, 5)
    
    def test_class_attributes_price_by_night(self):
        """ Tests related to class attributes """

        self.assertEqual(Place.price_by_night, 0)
        self.assertTrue(isinstance(Place.price_by_night, int))
        Place.price_by_night = 20
        self.assertEqual(Place.price_by_night, 20)
    
    def test_class_attributes_latitude(self):
        """ Tests related to class attributes """

        self.assertEqual(Place.latitude, 0.0)
        self.assertTrue(isinstance(Place.latitude, float))
        Place.latitude = 20.5
        self.assertEqual(Place.latitude, 20.5)
    
    def test_class_attributes_longitude(self):
        """ Tests related to class attributes """

        self.assertEqual(Place.longitude, 0.0)
        self.assertTrue(isinstance(Place.longitude, float))
        Place.longitude = 20.5
        self.assertEqual(Place.longitude, 20.5)
    
    def test_class_attributes_amenity_ids(self):
        """ Tests related to class attributes """

        self.assertEqual(Place.amenity_ids, [])
        self.assertTrue(isinstance(Place.amenity_ids, list))
        Place.amenity_ids = ["123-123"]
        self.assertEqual(Place.amenity_ids, ["123-123"])
