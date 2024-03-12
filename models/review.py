#!/usr/bin/python3
""" Contains the Review class """

from models.base_model import BaseModel


class Review(BaseModel):
    """ The Review class """

    place_id = ""
    user_id = ""
    text = ""

    def get_name(self):
        return "Review"
