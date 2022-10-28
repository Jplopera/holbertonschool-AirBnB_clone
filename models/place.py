#!/usr/bin/python3
"""Module that contains the class place inherited from class BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """the class defines Place
    Public class attributes:
        city_id (str): The id of the city.
        user_id (str): The id of the user.
        name (str): The name of the place.
        description (str): A description of the place.
        number_rooms (int): The number of rooms of the place.
        number_bathrooms (int): The number of bathrooms of the place.
        max_guest (int): The maximun numer of guests allowed in the place.
        price_by_night (int): Price for each night in the place.
        latitude (float): The latitud of the location of the place.
        longitude (float): The longitude of the location of the place.
        amenity_ids (list): the list containing the ids of the amenities.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = float(0)
    longitude = float(0)
    amenity_ids = []
