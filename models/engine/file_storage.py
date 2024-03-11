#!/usr/bin/python3
""" Contains the file sotrage handelrs """

import json
import os


class FileStorage:
    """ Handles storing objects into json files """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """

        return FileStorage.__objects

    def new(self, obj):
        """ Takes an object and stores it in teh __ojbects dictionary """

        obj_key = "{}.{}".format(obj.get_name(), obj.id)
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """

        try:
            with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
                objects_dict = {}
                for key, val in FileStorage.__objects.items():
                    objects_dict[key] = val.to_dict()
                json_rep = json.dumps(objects_dict)
                f.write(json_rep)

        except FileNotFoundError:
            print("File not found")

    def reload(self):
        """ Deserializes the JSON file to __objects """

        from ..base_model import BaseModel

        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
            json_data = f.read()
            objects_dict = json.loads(json_data)

        for obj_dict in objects_dict.values():
            obj = BaseModel(**obj_dict)
            self.new(obj)
