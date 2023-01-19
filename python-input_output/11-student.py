#!/usr/bin/python3
"""here pyhton module is documented"""


class Student:
    """this is class documatation"""

    def __init__(self, first_name, last_name, age):
        """this is constructore"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def to_json(self, attrs=None):
        """this is json"""
        for i in attrs:
            if type(attrs) == list and type(i) == str:
                return self.__dict__
        
    def reload_from_json(self, json):
        """this is reload_from_json"""
        for i, j in json.items():
            setattr(self, i, j)
