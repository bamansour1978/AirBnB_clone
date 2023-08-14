#!/usr/bin/python3
""" The Place class defines"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.

    Attributes:
        city_id : The City id (str).
        user_id : The User id (str)
        name : The name of the place (str)
        description : The description of the place(str)
        number_rooms: The number of rooms of the place (int)
        number_bathrooms : The number of bathrooms of the place  (int)
        max_guest : The maximum number of guests of the place  (int)
        price_by_night : The price by night of the place  (int)
        latitude : The latitude of the place (float)
        longitude : The longitude of the place (float)
        amenity_ids (list): A list of Amenity ids (float)
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
