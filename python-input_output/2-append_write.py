#!/usr/bin/python3
'''append function'''


def append_write(filename="", text=""):
    '''append function'''
    with open(filename, 'a', encoding="utf-8") as f:
        content = f.write(text)
    return len(text)
