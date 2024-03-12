#!/usr/bin/python3
""" Contains the State class """

from models.base_model import BaseModel


class State(BaseModel):
    """ The State class """

    name = ""

    def get_name(self):
        return "State"
