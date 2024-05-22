#!/usr/bin/python3
""""This is Class for rectangles"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        Rectangle.number_of_instances += 1

    def area(self):
        """Returns rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2*(self.__width + self.__height)

    @property
    def width(self):
        """"Returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def heigth(self):
        """"Returns height"""
        return self.__height

    @heigth.setter
    def height(self, value):
        """Sets the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Checks which Rectangle is bigger"""
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Returns a square"""
        return Rectangle(size, size)

    def __str__(self):
        """Prints a rectangle"""
        rec = ""
        if self.__height == 0 or self.__width == 0:
            return rec
        for i in range(self.__height):
            if i == self.__height - 1:
                rec += f"{self.print_symbol}" * self.__width
            else:
                rec += f"{self.print_symbol}" * self.__width + "\n"
        return rec

    def __repr__(self) -> str:
        """String representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")