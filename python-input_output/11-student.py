#!/usr/bin/python3
"""Student Class Module"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Instance definition"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """Converts instance to JSON format"""

        result = {}
        if attr is not None:
            for key, value in self.__dict__.items():
                if key in attr:
                    result[key] = value
        else:
            return object.__dict__

    def reload_from_json(self, json):
        """Resets the attributes to default"""
        
        for key, value in json.__dict__.items():
            setattr(self, key, value)
