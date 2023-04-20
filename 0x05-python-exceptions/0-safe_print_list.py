#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """prints x elements of the list my_list
    args:
        my_list (list): a list to print
        x (int): number of the list elemets to print
    return:
        number of printed elements
    """
    n = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]))
            n += 1
        except IndexError:
            break
    print(" ")
    return(n)