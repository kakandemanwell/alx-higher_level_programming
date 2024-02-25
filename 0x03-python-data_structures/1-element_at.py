#!/usr/bin/python3

def element_at(my_list, idx):
    """"
    retrives an element from a list at position idx
    args:
        my_list (list)
        idx (int): position of element to retrieve
    """
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
