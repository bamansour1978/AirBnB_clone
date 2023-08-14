#!/usr/bin/python3
"""The User class define."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.

    Attributes:
        email : The email of the user. (str)
        password : The password of the user. (str)
        first_name : The first name of the user. (str)
        last_name : The last name of the user. (str)
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
