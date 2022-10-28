#!/usr/bin/python3
"""Module that contains Base class"""


import uuid
import datetime
import models


class BaseModel:
    """class BaseModel that defines all common attributes/methods
    for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel"""
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """__str__ method that returns a string"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with the current
        datetime"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the
        instance"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        return my_dict
