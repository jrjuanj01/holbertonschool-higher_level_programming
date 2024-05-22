#!/usr/bin/python3
"""A class that inherits from the rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A subclass of rectangle"""
    
    def __init__(self, size):
        """Instancialization of a Square"""
        
        super().integer_validator("size", size)
        self.__size = size
    
    def area(self):
        """Returns the area of the square"""
        
        return (self.__size ** 2)
