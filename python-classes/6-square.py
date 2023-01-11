#!/usr/bin/python3
"""This is classes and object .Module is documented is showing"""


class Square:
    """This is Square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """size"""
        return self.__size

    @size.setter
    def size(self, value):
        """size value"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """position"""
        return self.__position

    @position.setter
    def position(self, value):
        """this is position"""
        if type(value) != tuple or type(value[0]) != int or type(value[1]) != int or value >= 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value
    
    def area(self):
        """Hiii"""
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                if self.__position[1] >= 0:
                    print(" " * self.__position[0], end="")
                print("#" * self.__size)
                print("")
