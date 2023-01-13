#!/usr/bin/python3
""" this is module documented """


class BaseGeometry:
    """ This is base class documentation """

    def area(self):
        """ This is public instance documentation """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validator documented """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            pass
