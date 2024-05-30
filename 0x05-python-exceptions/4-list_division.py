#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                result_list.append(0)
            else:
                a = my_list_1[i]
                b = my_list_2[i]
                if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
                    print("wrong type")
                    result_list.append(0)
                else:
                    result_list.append(a / b)
        except ZeroDivisionError:
            print("division by 0")
            result_list.append(0)
        except Exception as e:
            print("unexpected error:", e)
            result_list.append(0)
    
    return result_list
