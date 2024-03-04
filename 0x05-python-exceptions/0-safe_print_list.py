#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """prints x elements of the list my_list
    args:
        my_list (list): a list to print
        x (int): number of the list elemets to print
    return:
        number of printed elements
    """
    count = 0

    for item in my_list:
        if count < x:
            try:
                print("{}".format(item), end="")
                count += 1
            except IndexError:
                print()
                return count
    print()
    return count
