#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """This function divides elements by elements in 2 lists."""
    result = []
    try:
        for i in range(list_length):
            try:
                if isinstance(my_list_1[i], (int, float)) and \
                        isinstance(my_list_2[i], (int, float)):
                    result.append(my_list_1[i] / my_list_2[i])
                else:
                    result.append(0)
                    print("wrong type")
            except ZeroDivisionError:
                result.append(0)
                print("division by 0")
    except IndexError:
        print("out of range")
    finally:
        while len(result) < list_length:
            result.append(0)
        return result
