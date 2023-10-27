#!/usr/bin/python3
"""Create a class name Square"""


class Square:
    """define __init__ function"""
    def __init__(self, size=0):
        """initiate size of self to size"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Conditional if statement"""
        if type(value) is not int:
            """raise error"""
            raise TypeError("size must be an integer")
        elif value < 0:
            """raise value error"""
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
            """define area function"""
    def area(self):
        """return area"""
        return self.__size ** 2
    """define myprint function"""
    def my_print(self):
        """if conditional statement"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
