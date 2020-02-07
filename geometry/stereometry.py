

"""The module is consists of classes for 3D figures"""
"""Modules and packages (for the code in practice.py)"""

from math import pi, pow


class Cuboid:
    """Class Cuboid\nThe constructor gets 3 arguments (length, width and height)"""
    def __init__(self, a, b, c):
        self.length = a
        self.width = b
        self.height = c
        self.__squareSurface =  2 * (a*b + a*c + b*c)
        self.__volume = a * b * c

    def S(self):
        """Method for calculation the square of surface of cuboid"""
        return round(self.__squareSurface, 2)

    def V(self):
        """Method for calculation the volume of cuboid"""
        return round(self.__volume, 2)


class Ball:
    """Class Ball\nThe constructor gets 1 argument (radius)"""
    def __init__(self, radius):
        self.r = radius

    def S(self):
        """Method for calculation the square of ball"""
        s = 4 * pi * pow(self.r, 2)
        return round(s, 2)

    def V(self):
        """Method for calculation the volume of ball"""
        v = (4 / 3) * pi * pow(self.r, 3)
        return round(v, 2)


