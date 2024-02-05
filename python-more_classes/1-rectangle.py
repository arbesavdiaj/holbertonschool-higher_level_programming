#!/usr/bin/python3
'''
create a class rectangle
'''


class Rectangle:
    '''
    class Rectangle
    '''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        return self.width
    
    @width.setter
    def width(self, value):
        self.__width = value
    if not isinstance(width, int):
        raise TypeError("width must be an integer")
    if width < 0:
        raise ValueError("width must be >= 0")
    
    def height(self):
        self.__height = self
    
    @property
    def height(self):
        return self.height
    
    @height.setter
    def height(self, value):
        self.__height = value
    if height < 0:
        raise ValueError("height must be >= 0")
