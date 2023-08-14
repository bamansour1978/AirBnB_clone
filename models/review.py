#!/usr/bin/python3
"""The Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.

    Attributes:
        place_id : The Place id. (str)
        user_id : The User id. (str)
        text : The text of the review. (str)
    """

    place_id = ""
    user_id = ""
    text = ""
