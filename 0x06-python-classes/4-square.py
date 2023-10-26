#!/usr/bin/python3
"""Create a class Square"""


class Square:
    """define init"""
    def __init__(self, size=0):
        """initialize self"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Conditional if statement"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            """initialize size with value"""
            self.__size = value
            """define area function"""
    def area(self):
        """return area of a square"""
        return self.__size ** 2
