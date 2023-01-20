#!/usr/bin/python3
"""module is documented"""
from models.base import Base


class Rectangle(Base):
    """ this is rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width"""
        return self.__width

    @property
    def height(self):
        """height"""
        return self.__height

    @property
    def x(self):
        """x"""
        return self.__x

    @property
    def y(self):
        """y"""
        return self.__y

    @width.setter
    def width(self, value):
        """width"""
         if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value <= 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value <= 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = value
