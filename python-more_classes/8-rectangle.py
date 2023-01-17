[23:52, 1/16/2023] Geetanjali behera Nth: #!/usr/bin/python3
"""
This is the "Rectangle"  module.
This module provides a Rectangle class.
"""


class Rectangle:
    """A Rectangle class with attributes width and height,
    methods area, perimeter, print, str, repr, and del, and
    class attribute number_of_instances that keeps track of # of instances,
    class attribute print_symbol which is used as symbol for printing,
    and static method bigger_or_equal that returns biggest rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def _init_(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
[23:57, 1/16/2023] Geetanjali behera Nth: def _repr_(self):
        return "Rectangle({:d}, {:d})".format(self._width, self._height)

    def _str_(self):
        total = ""
        for i in range(self.__height):
            for j in range(self.__width):
                try:
                    total += str(self.print_symbol)
                except Exception:
OBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOB                    total += type(self).print_symbol
OBOB            if i is not self.__height - 1:
OBOBOB                total += "\n"
        return total
OBOBOB
    def _del_(self):
OB        print("Bye rectangle...")
OBOBOB        Rectangle.number_of_instances -= 1
OBOB
    def area(self):
OBOB        return self._width * self._height
[6~OBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOB
OBOBOBOB    def perimeter(self):
        if self._width is 0 or self._height is 0:
OB            return 0
OBOBOBOB        return (4 * self._width) + (2 * self._height)
