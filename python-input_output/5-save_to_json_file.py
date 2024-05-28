#!/usr/bin/python3
""" A function that returns a JSON Object in a file"""
import json


def save_to_json_file(my_obj, filename):
    """Returns a JSON file"""
    
    return json.dump(my_obj, filename)
