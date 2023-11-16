#!/usr/bin/python3
"""class module"""
import json

class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialise Private attribute"""
        self.id = id
        if id is not None:
            Base.__nb_object += 1
            self.id = Base.__nb_object
