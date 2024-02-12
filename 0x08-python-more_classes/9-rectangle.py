#!/usr/bin/python3
""" 
empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """ 
    class rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ 
        Instantiation with optional width and height
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    @staticmethod
    def __validate_dimension(value, dimension):
        """ 
        validate dimension
        """
        if not isinstance(value, int):
            raise TypeError(f"{dimension} must be an integer")
        if value < 0:
            raise ValueError(f"{dimension} must be >= 0")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

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

    def __str__(self):
        """ 
        return the rectangle with the character #
        """
        if self.width == 0 or self.height == 0:
            return ""
        return ("\n".join(["".join([str(self.print_symbol)
                for i in range(self.width)]) for j in range(self.height)]))

    def __repr__(self):
        """ 
        return a string representation of the rectangle
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """ 
        Print the message when an instance of Rectangle is deleted
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(repr(my_rectangle))

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(repr(my_rectangle))

    del my_rectangle

    print(Rectangle.number_of_instances)

