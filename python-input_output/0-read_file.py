#!/usr/bin/python3
'''a function that reads a file'''


def read_file(filename=""):
    '''reads a file'''
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end="")
