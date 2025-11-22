#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element two lists up to list_length.
    Returns a new list with the results. Handles exceptions."""
    result = []
    for i in range(list_length):
        value = 0
        try:
            a = my_list_1[i]
            b = my_list_2[i]

            if (not isinstance(a, (int, float)) or
                    not isinstance(b, (int, float))):
                raise TypeError("wrong type")

            value = a / b
        except ZeroDivisionError:
            print("division by 0")
            value = 0
        except TypeError:
            print("wrong type")
            value = 0
        except IndexError:
            print("out of range")
            value = 0
        finally:
            result.append(value)
    return result
