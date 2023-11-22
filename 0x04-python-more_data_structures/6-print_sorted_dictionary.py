#!/usr/bin/python3
"""Prints a dictionary by ordered keys"""


def print_sorted_dictionary(a_dictionary):
    for members in sorted(a_dictionary.keys()):
        print(f"{members}: {a_dictionary[members]}")
