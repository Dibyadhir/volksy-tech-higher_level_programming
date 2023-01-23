#!/usr/bin/python3
"""this is module document"""


class Rectangle(Base):
    """this is rectangle """

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

    def area(self):
        """its return area of the rectangle"""
        return self.width * self.height

    def display(self):
        """it prints in stdout the rectangle"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        for i in range(self.y):
            print("")
        for i in range(self.height):
            [print(" ", end="") for j in range(self.x)]
            [print("#",end="") for k in range(self.width)]
            print("")

    def display(self):
        """Rectangle instance with the character #."""
        print('\n' * self.y, end='')
        for height in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def update(self, *args, **kwargs):
        """this is args"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
            """it overriding the __str__ method"""
            return "[Rectangle]{} {}/{} - {}/{}".format
        (self.id, self.x, self.y, self.width, self.height)
