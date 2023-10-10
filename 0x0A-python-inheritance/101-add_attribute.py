#!/usr/bin/python3
"""Selective addition"""


def add_attribute(obj, att, val):
    """
        Adds a new attribute to an object when possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, val)
