#!/usr/bin/python3
""" The Amenity class define."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Rep an amenity.

    Attributes:
        name : The name of the amenity (str).
    """

    name = ""
