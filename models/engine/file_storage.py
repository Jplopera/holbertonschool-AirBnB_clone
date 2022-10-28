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
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        dict1 = {}
        for key, value in FileStorage.__objects.items():
            dict1.update([(key, value.to_dict())])

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(dict1))

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                str1 = f.read()

                fromjson = json.loads(str1)
                FileStorage.__objects = {key: eval(f"{val['__class__']})(**{val})") for key, val in fromjson.items()}
