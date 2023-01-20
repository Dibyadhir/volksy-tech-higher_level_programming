#!/usr/bin/python3
"""module is documented"""
import models.base import Base


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
        self.__width = value

    @height.setter
    def height(self, value):
        """height"""
        self.__height = value

    @x.setter
    def x(self, value):
        """x"""
        self.__x = value

    @y.setter
    def y(self, value):
        """y"""
        self.__y = value
