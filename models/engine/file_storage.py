#!/usr/bin/python3
"""Module that contains FileStorage class"""


import json
from models.base_model import BaseModel
import os


class FileStorage:
    """class FileStorage that serializes instances to a JSON file and
    deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            data = {key: v.to_dict() for key, v in self.__objects.items()}
            json.dump(data, file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                json_dict = json.loads(file.read())
                for key, v in json_dict.items():
                    self.__objects[key] = eval(v['__class__'])(**v)
