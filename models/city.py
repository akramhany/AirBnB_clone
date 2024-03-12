#!/usr/bin/python3
""" Contains the City class """

from models.base_model import BaseModel


class City(BaseModel):
    """ The City class """

    state_id = ""
    name = ""

    def get_name(self):
        return "City"
