#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists elmnt by elmnt.

    Args:
        my_list_1 (list): The firrst list.
        my_list_2 (list): The secnd list.
        list_length (int): The num of elmnts to divide.

    Returns:
        A new list of lngth list_length containg all divisns.
    """
    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
