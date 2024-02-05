#!/usr/bin/python3
'''
create a class rectangle
'''


class Rectangle:
    '''
    class Rectangle
    '''
    def width(self):
        self.__width = self
    
    @width.setter
    def width(self, value):
        self.__width = value
    if width is not isinstance(int):
        raise TypeError("width must be an integer")
    if width < 0:
        raise ValueError("width must be >= 0")
    
    def height(self):
        self.__height = self
    
    @height.setter
    def height(self, value):
        self.__height = value
    if height < 0:
        raise ValueError("height must be >= 0")
