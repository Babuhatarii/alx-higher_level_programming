#!/usr/bin/python3
"""
Module containing the Rectangle class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance."""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height
