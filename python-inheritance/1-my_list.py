#!/usr/bin/python3
"""
This module defines the MyList class, a subclass of list with
an additional method to print the list sorted.
"""


class MyList(list):
    """A custom list class that can print itself sorted."""

    def print_sorted(self):
        """Print the list in ascending sorted order and return it."""
        sorted_list = sorted(self)
        print(sorted_list)
        return sorted_list
