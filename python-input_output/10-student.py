#!/usr/bin/python3
"""here python module is docuented"""


class Student:
    """this is class documatation"""

    def __init__(self, first_name, last_name, age):
        """this is constructore"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """this is json"""
        if attrs is None:
            return self.__dict__
        else:
            x = dict()
            for i in attrs:
                if i in self.__dict__:
                    x[i] = self.__dict__.get(i)
            return x
