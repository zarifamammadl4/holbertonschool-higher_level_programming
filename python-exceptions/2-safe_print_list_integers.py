#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of my_list if they are integers.
    Returns the number of integers printed."""
    count = 0
    i = 0
    while i < x:
        try:
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                count += 1
        except IndexError:
            # Stop if index goes out of range
            break
        i += 1
    print()
    return count
