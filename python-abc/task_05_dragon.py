#!/usr/bin/python3
"""The Mystical Dragon - Mastering Mixins"""


class SwimMixin():
    """Swim Class"""
    
    def swim(self):
        print("The creature swims!")

class FlyMixin():
    """Fly Class"""
    
    def fly(self):
        print("The creature flies!")
    
class Dragon(SwimMixin, FlyMixin):
    """Dragon that inherits from both SwimMixin and FlyMixin"""
    
    def roar(self):
        print("The dragon roars!")
