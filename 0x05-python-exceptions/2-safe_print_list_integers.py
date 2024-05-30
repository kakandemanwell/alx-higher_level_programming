#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    prints the first x elements of a list and only integers.\
    args:
    my_list (list): list os elements to be printed
    x (int): number of elements to be printed
    return: number of elemts printed
    """
    count = 0
    printed = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except (ValueError, TypeError):
                continue
            finally:
                printed += 1
    except IndexError:
        raise IndexError("List index out of range")
    print()
    return count