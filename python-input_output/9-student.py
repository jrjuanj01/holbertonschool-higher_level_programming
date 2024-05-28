#!/usr/bin/python3
"""Student Class Module"""


class Student:
    """Student class"""
    
    def __init__(self, first_name, last_name, age):
        """Instance definition"""
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def to_json(self):
        """Converts instance to JSON format"""
        result = {}
        for key, value in self.__dict__.items():
            result[key] = value
        return result
