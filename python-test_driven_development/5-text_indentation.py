#!/usr/bin/python3

def text_indentation(text):

    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end='')
        if text[i] in ['.', '?', ':']:
            print("\n\n", end='')
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
