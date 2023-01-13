#!/usr/bin/python3
""" this is method validation """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """ here method is documented """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ this is public method """
        return self.__height * self.__width
    def __str__(self):
        """ this is str constructure """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
