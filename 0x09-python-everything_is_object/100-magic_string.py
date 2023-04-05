#!/usr/bin/python3
n = 0
def magic_string():
    global n
    n += 1
    res = ""
    for i in range(n):
        if i + 1 == n:
            res += "Best School"
        else:
            res += "Best School, "
    return res
