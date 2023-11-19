#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """replaces all occurances of an element by another in a new list"""
    new_list = []
    """creates a new list to store the elements to be replaced"""
    for element in my_list:
        """itereates over each element in the list"""
        element = replace if element == search else element
        """if element matches the search element, append the replacement
        to the new list else append the original element to the new list"""
        new_list.append(element)
    return new_list
