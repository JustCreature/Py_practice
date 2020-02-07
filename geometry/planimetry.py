

"""The module is consists of classes for plain figures"""
"""Modules and packages (for the code in practice.py)"""

from math import pi, pow


class Rectangle:
    """Class Rectangle\nThe constructor gets 2 arguments (width and height)"""
    def __init__(self, a, b):
        self.width = a
        self.height = b

    def square(self):
        """Method for calculation the square of rectangle"""
        return round(self.width * self.height, 2)

    def perimeter(self):
        """Method for calculation the perimeter of rectangle"""
        return 2 * (self.width + self.height)


class Circle:
    """Class Circle\nThe constructor gets 1 argument (radius)"""
    def __init__(self, radus):
        self.r = radus

    def square(self):
        """Method for calculation the square of circle"""
        return round(pi * pow(self.r, 2), 2)

    def length(self):
        """Method for calculation the length of circle"""
        return round(2 * pi * self.r)


