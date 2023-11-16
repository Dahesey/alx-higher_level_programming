#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base

class Rectangle(Base):
    """Rectangle Model"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize attributes"""
        super.__init__(id)
        self.width = width
        self.height = width
        self.x = x
        self.y = y
