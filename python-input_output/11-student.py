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
            for key, value in self.__dict__.items():
                result[key] = value
        return result

    def reload_from_json(self, json):
        """Resets the attributes to default"""

        for attr, vlaue in self.__dict__.items():
            for key, default in json.__dict__.items():
                value = default
