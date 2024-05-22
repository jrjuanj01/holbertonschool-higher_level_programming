#!/usr/bin/python3
"""A class Rectangle that inherits from BaseGeometry"""


BaseGeomerty = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeomerty):
    """Class of Rectangle"""

    def __init__(self, width, height):
        """Initialization of a rectangle"""

        super().integer_validator(self, width)
        self.__width = width

        super().integer_validator(self, height)
        self.__height = height
