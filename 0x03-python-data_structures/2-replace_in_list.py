#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    replaces an element of a list at aspecific position.
    args:
        my_list (list): list of element s to replace.
        idx (int): integer position of the element
        element (any): element to replace
    """
    if idx < 0:
        return my_list
    if idx > len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return (my_list)
