#!/usr/bin/python3
"""Defines a class that inherits from int"""


class MyInt(int):
    """And overides == and !="""

    def __eq__(self, value):
        """Overides == operator"""
        return self.__value != value
    
    def __ne__(self, value):
        """overides the != operator"""
        return self.__value == value
