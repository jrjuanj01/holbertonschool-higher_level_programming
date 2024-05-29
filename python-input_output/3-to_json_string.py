#!/usr/bin/python3
""" A function that returns the JSON Object String"""
import json


def to_json_string(my_obj):
    """Returns a JSON string"""

    return json.dumps(my_obj)
