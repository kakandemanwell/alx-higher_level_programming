#!/usr/bin/python3

def safe_print_list_integer(my_list=[], x=0):
    """
    safly prints list integers
    args:
    my_list (list): list os elements to be printed
    x (int): number of elements to be printed
    return: number of elemts printed
    """
    count = 0
    try:
        for i in range(x):
            try:
                value = my_list[i]
                if isinstance(value, int):
                    print("{:d}".format(value), end="")
                    count += 1
            except (IndexError):
                pass
    finally:
        print('')
        return (count)
