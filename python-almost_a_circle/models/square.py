#!/usr/bin/python3
"""this is module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this is square"""

    def __init__(self, size, x=0, y=0, id=None):
        """ this is new Square."""
        super().__init__(self, size, x, y, id)

    def __str__(self):
        """representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format
                 (self.id, self.x, self.y,self.width)
