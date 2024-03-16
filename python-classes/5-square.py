#!/usr/bin/python3
'''
Write a class Square that defines a square by: (based on 0-square.py)
'''


class Square:
    '''
    not passing any arguments
    '''
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        if self.__size == 0:
            print()
        for _ in range(self.__size):
            print('#' * self.__size)
