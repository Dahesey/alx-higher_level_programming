#!/usr/bin/python3
"""Create a class Square"""


class Square:
    """Initialise with self and instantiate size"""
    def __init__(self, size=0):
        """If conditional statements"""
        if type(size) != int:
            """Raise type error"""
            raise TypeError("size must be an integer")
        elif size < 0:
            """Raise Value error"""
            raise ValueError("size must be >= 0")
        else:
            """Create private instance attribute"""
            self.__self = size
            """Create a public instance method"""
    def area(self):
        """returns area"""
        return self.__self ** 2
