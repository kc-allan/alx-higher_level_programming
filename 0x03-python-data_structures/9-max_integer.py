#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return ("None")
    else:
        for i in my_list:
            n = my_list[0]
            if i > n:
                n = i
    return (n)
