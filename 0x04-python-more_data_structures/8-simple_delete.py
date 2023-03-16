#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    try:
        a_dictionary[key]
    except KeyError:
        return a_dictionary
    del(a_dictionary[key])
    return a_dictionary
