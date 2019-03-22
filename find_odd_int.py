#! /usr/bin/env python
# Given an array, find the int that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.


def find_odd(int_list):
    """return None if no odd int was found, the odd one otherwise"""
    for k in int_list:
        if int_list.count(k) % 2:
            return k
    return None
