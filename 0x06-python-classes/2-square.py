#!/usr/bin/python3
"""square defination"""


class Square:
    """ square with private instance attribute size """
    def __init__(self, size=0):
        """
        Args:
            size: size of square
        """

        self.__size = size
        self.__validate_size()

    def __validate_size(self):
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
