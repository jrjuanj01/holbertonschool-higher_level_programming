#!/usr/bin/python3
"""Function that returns an object from JSON String"""
import json


def from_json_string(my_str):
    """Converts JSON String into an object"""
 
    return json.loads(my_str)
