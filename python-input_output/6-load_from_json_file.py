#!/usr/bin/python3
""" A function that returns an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """Returns an object from JSON file"""

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
