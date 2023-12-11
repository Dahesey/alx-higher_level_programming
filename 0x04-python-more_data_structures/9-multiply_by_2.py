#!/usr/bin/python3
"""Returns a new dictionary with all values multiplied by 2"""


def multiply_by_2(a_dictionary):
    """returns a new dictionary with all its values multiplied by 2"""
    return{key: value * 2 for key, value in a_dictionary.items()}