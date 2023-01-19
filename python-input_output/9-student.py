#!/usr/bin/python3
"""here module is documented"""


class Student:
    """this is class documatation"""

    def __init__(self, first_name, last_name, age):
        """this is constructore"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """this is documented"""
        return self.__dict__
