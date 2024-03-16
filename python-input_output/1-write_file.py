#!/usr/bin/python3
'''a function that writes in a file'''


def write_file(filename="", text=""):
    '''writes a file'''
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    return len(text)
