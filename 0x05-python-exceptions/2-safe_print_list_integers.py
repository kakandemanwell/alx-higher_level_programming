#!/usr/bin/python3

def safe_print_list_integer(my_list=[], x=0):
    """
    safly prints list integers
    args:
    my_list (list): list os elements to be printed
    x (int): number of elements to be printed
    return: number of elemts printed
    """
    n = 0
    for i in range(x):
        try:
            print("{:d}". format(my_list[i]))
            n += 1
        except (ValueError, TypeError):
            continue
    return(n)
