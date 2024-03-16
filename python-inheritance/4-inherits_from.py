#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that inherited from
    the specified class, otherwise False"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
