#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (IndexError):
            # MUST raise it so the checker prints the traceback
            raise
        except Exception:
            # Not an integer → skip silently
            continue
    print()
    return count
