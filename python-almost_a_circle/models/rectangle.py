#!/usr/bin/python3
'''base class'''
from .base import Base


class Rectangle(Base):
    '''constructor'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError(f"width must be an integer")
        if value in ["width", "height"] and value <= 0:
            raise ValueError(f"width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError(f"height must be an integer")
        if value in ["width", "height"] and value <= 0:
            raise ValueError(f"width must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError(f"width must be an integer")
        if value in ["x", "y"] and value < 0:
            raise ValueError(f"width must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError(f"width must be an integer")
        if value in ["x", "y"] and value < 0:
            raise ValueError(f"width must be >= 0")
        self.__y = value
