#!/usr/bin/python3
""" A function that returns an Object from a JSON file"""
import json


def load_from_json_file(my_obj, filename):
    """Returns an object from JSON file"""

    with open(filename, "w", encoding="utf-8") as f:
        json.load(my_obj, f)
