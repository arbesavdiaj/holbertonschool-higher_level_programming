#!/usr/bin/python3
'''base class'''


class Base:
    '''base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        if id is None:
            Base.__nb_objects += 1
