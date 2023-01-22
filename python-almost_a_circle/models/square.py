#!/usr/python3
"""this is module"""
from rectangle import Rectangle


class Square(Rectangle):
    """this is square"""
    def __init__(self, size, x=0, y=0, id=None):
        """ this is new Square."""
        super().__init__(size, size, x, y, id)
