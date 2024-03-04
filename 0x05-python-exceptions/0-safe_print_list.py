#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """prints x elements of the list my_list
    args:
        my_list (list): a list to print
        x (int): number of the list elemets to print
    return:
        number of printed elements
    """
    try:
        count = 0
        for i in range(x):
            print(my_list[i], end=' ')
            count += 1
    except IndexError:
        pass
    finally:
        print()
    return count
