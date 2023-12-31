#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Model"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize attributes"""
        super().__init__(id)
        self.width = width
        self.height = width
        self.x = x
        self.y = y

    @property
    def width(self):
        """retrieving width private attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """retrieving height private attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Retrieving x private instance attributes"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """retrieving y private instance attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """return the area of the public instance attribute rectangle"""
        return self.__height * self.__width

    def display(self):
        print('\n'*self.y, end="")
        for _ in range(self.height):
            print(''*self.x + '#'*self.width)
