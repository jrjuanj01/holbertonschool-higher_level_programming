#!/usr/bin/python3
"""Opens and writes a file"""


def write_file(filename="", text=""):
    """Opens, reads, and prints the file given"""

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
