#!/usr/bin/python3
'''json file'''


import json


def load_from_json_file(filename):
    '''json file'''
    with open(filename, encoding="utf-8") as f:
        data = json.load(f)
        return data
