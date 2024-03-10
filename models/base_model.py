#!/usr/bin/python3
"""
Contains the implementation of the base model class, which all classes
would inherit from.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    The base class which contain all the common attributes/methods
    for all the classes.
    """

    def __init__(self):
        """
        initialize all the attributes of the class.
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        prints info about the class.
        """

        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """
        saves the data of the class, and update the updated_at
        with the current datetime.
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """

        inst_dict = self.__dict__
        inst_dict["__class__"] = "BaseModel"
        d_format = "%Y-%m-%dT%H:%M:%S.%f"
        inst_dict["created_at"] = inst_dict["created_at"].strftime("d_format")
        inst_dict["updated_at"] = inst_dict["updated_at"].strftime("d_format")
        return inst_dict
