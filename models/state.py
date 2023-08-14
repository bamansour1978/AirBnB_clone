#!/usr/bin/python3
"""The State class define."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state.

    Attributes:
        name : The name of the state. (str)
    """

    name = ""
