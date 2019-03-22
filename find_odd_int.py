#! /usr/bin/env python
# Given an array, find the int that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.


def find_odd(int_list):
    """return None if no odd int was found, the odd one otherwise"""
    my_dict = dict.fromkeys([k for k in set(int_list)])
    for k in my_dict:
        my_dict[k] = int_list.count(k)
    for k in my_dict:
        if my_dict[k] % 2 != 0:
            return k
    return None
