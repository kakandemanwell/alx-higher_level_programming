#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    prints all integers of a llist in reverse order
    args:
        my_list (list): list to reverse
    """
    if not my_list:
        pass
    else:
        my_list.reverse()
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]))
