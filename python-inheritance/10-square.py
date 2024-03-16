#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""
    def __init__(self, size):
        Rectangle.integer_validator(self, "size",  size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
