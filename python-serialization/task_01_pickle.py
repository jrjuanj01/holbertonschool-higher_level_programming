#!/usr/bin/python3
"""Custom Object Class Module"""
import pickle


class CustomObject:
    """Custom Object class"""
    
    def __init__(self, name="", age=0, is_student=False):
        """Instance definition"""

        self.name = name
        self.age = age
        self.is_student = is_student


    def display(self):
        """Displays the class attribute values"""

        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize instance and save to thr given file"""

        with open(filename, "wb") as pfile:
            pickle.dump(self, pfile)


    @classmethod
    def deserialize(cls, filename): 
        """Create an instance from the given pickle file"""

        try:
            with open(filename, "rb") as pfile:
                return pickle.load(pfile)
        except (FileNotFoundError) as e:
            return None