#!/usr/bin/python3
"""Module that contains the class city inherited from class BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """The class defines City
    Public class attributes:
        state_id (str): The id of the state of the city.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
