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

    def __init__(self, *args, **kwargs):
        """
        initialize all the attributes of the class.
        """

        from models.__init__ import storage

        d_format = "%Y-%m-%dT%H:%M:%S.%f"
        if not args and kwargs:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(val, d_format))
                elif key != "__class__":
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        prints info about the class.
        """

        return "[{}] ({}) {}".format(self.get_name(), self.id, self.__dict__)

    def save(self):
        """
        saves the data of the class, and update the updated_at
        with the current datetime.
        """

        from models.__init__ import storage

        self.updated_at = datetime.now()
        storage.save()

    def update(self, attr_name, attr_value):
        """ Takes an attribute name and a value and updates it """

        if hasattr(self, attr_name):
            if isinstance(self.__dict__[attr_name], int):
                self.__dict__[attr_name] = int(attr_value)
            elif isinstance(self.__dict__[attr_name], float):
                self.__dict__[attr_name] = float(attr_value)
            else:
                self.__dict__[attr_name] = str(attr_value)
        else:
            self.__dict__[attr_name] = str(attr_value)

    def get_name(self):
        """ Returns the class name """

        return "BaseModel"

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """

        inst_dict = {}
        for key in self.__dict__:
            inst_dict[key] = self.__dict__[key]
        inst_dict["__class__"] = self.get_name()
        d_format = "%Y-%m-%dT%H:%M:%S.%f"
        inst_dict["created_at"] = inst_dict["created_at"].strftime(d_format)
        inst_dict["updated_at"] = inst_dict["updated_at"].strftime(d_format)
        return inst_dict
