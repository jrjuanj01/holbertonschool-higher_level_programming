#!/usr/bin/python3
"""A class that inherits from List"""


class MyList(list):
    """New Class"""

    def __init_subclass__(cls, value=None):
        """Initializes Subclass list"""

        cls.list = value
        return super().__init_subclass__()

    def print_sorted(self):
        """A Method that prints the inherited attributes"""

        print(f"{sorted(self)}")
