#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i, k in sorted(a_dictionary.items()):
        print("{}: {}".format(i, k))
