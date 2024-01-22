#!/usr/bin/python3
""" Finds a peak inside a list """


def find_peak(list_of_integers):
    if list_of_integers == []:
        return None
    max = list_of_integers[0]
    for item in list_of_integers:
        if item > max:
            max = item
    return max
