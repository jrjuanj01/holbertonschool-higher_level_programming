#!/usr/bin/python3
"""Opens and reads file"""


def read_file(filename=""):
    """Opens, reads, and prints the file given"""

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
