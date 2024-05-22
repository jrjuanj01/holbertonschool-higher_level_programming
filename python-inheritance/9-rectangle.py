#!/usr/bin/python3
"""A class Rectangle that inherits from BaseGeometry"""


BaseGeomerty = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeomerty):
    """Class of Rectangle"""

    def __init__(self, width, height):
        """Initialization of a rectangle"""

        super().integer_validator("width", width)
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height 

    def area(self):
        """Returns rectangle area"""
        return (self.__width * self.__height)

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
