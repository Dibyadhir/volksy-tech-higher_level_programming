#!/usr/bin/python3
"""here module is documented"""

class Base:
    """this is my class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects =  __nb_objects + 1
            self.id =  Base.__nb_objects
