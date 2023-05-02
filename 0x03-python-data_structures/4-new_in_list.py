#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    replaces an element in a list at a specific position
    without modifying the original list
    args:
        my_list(list): list of elements
        idx (int): position of new element
        element(int): element to replace
    """
    if idx < 0:
        return my_list
    if idx > len(my_list):
        return my_list
    else:
        copy = [el for el in my_list]
        copy[idx] = element
        return (copy)
