#!/usr/bin/python3
""" 
empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """ 
    class rectangle
    """

    def __init__(self, width=0, height=0):
        """ 
        Instantiation with optional width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ 
        width
        """
        return self.__width

    @property
    def height(self):
        """ 
        height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ 
        width setter
        """
        self.__validate_dimension(value, "width")
        self.__width = value

    @height.setter
    def height(self, value):
        """ 
        height setter
        """
        self.__validate_dimension(value, "height")
        self.__height = value

    def __validate_dimension(self, value, dimension):
        """ 
        validate dimension
        """
        if not isinstance(value, int):
            raise TypeError(f"{dimension} must be an integer")
        if value < 0:
            raise ValueError(f"{dimension} must be >= 0")

    def area(self):
        """ 
        returns rectangle area
        """
        return self.width * self.height

    def perimeter(self):
        """ 
        returns rectangle perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
