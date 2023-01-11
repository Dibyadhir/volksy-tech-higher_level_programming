#!/usr/bin/python3
""" This is class and object. """


class Square:
    """ this is square. """

    
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        try:
            if type(value) != tuple and  type(value[0]) != int and type(value[1]) != int:
                raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
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
