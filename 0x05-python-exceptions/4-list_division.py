#!/usr/bin/python3
def list_division(my_list1, my_list2, list_length):
    """
    args:
    my_list1 (list): a list to divide
    my_list2 (list): a list to divide(denominator)
    return:
    returns a new_list with division results
    """
    new_list = []
    for i in range(list_length):
        try:
            div = my_list1[i] / my_list2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by zero")
            div = 0
        except IndexError:
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
