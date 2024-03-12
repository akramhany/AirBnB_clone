#!/usr/bin/python3
""" Contains the User class """

from models.base_model import BaseModel


class User(BaseModel):
    """ The User class """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def get_name(self):
        return "User"
