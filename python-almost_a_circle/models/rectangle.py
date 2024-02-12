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
        self.__width = value
        if not isinstance(value, int):
            raise TypeError(f"width must be an integer")
        if value in ["width", "height"] and value <= 0:
            raise ValueError(f"width must be > 0")
        if value in ["x", "y"] and value < 0:
            raise ValueError(f"width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError(f"height must be an integer")
        if value in ["width", "height"] and value <= 0:
            raise ValueError(f"width must be > 0")
        if value in ["x", "y"] and value < 0:
            raise ValueError(f"height must be >= 0")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value
        if not isinstance(value, int):
            raise TypeError(f"width must be an integer")
        if value in ["width", "height"] and value <= 0:
            raise ValueError(f"width must be > 0")
        if value in ["x", "y"] and value < 0:
            raise ValueError(f"width must be >= 0")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
        if not isinstance(value, int):
            raise TypeError(f"width must be an integer")
        if value in ["width", "height"] and value <= 0:
            raise ValueError(f"width must be > 0")
        if value in ["x", "y"] and value < 0:
            raise ValueError(f"width must be >= 0")
