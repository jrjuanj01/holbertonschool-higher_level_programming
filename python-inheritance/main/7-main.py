#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    bg.integer_validator("my_int", 12)
    print(f"{bg.name} is {bg.value}")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))  

try:   
    bg.integer_validator("width", 89)
    print(f"{bg.name} is {bg.value}")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
