#!/usr/bin/python3
"""creating a class with name Square"""


class Square:
    """Initiate with init self"""
    def __init__ (self, size=0):
        """If conditional statements"""
        if type(size) != int:
            """Raise Typeerror is size is not an integer"""
            raise TypeError("size must be an integer")
        elif size < 0:
            """Raise Valueerror if size is less than 0"""
            raise ValueError("size must be >= 0")
        else:
            """Create private instance attribute and instantiate to self"""
            self.__size = size
