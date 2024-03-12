#!/usr/bin/python3
""" Contains the Amenity class """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ The Amenity class """

    name = ""

    def get_name(self):
        return "Amenity"
