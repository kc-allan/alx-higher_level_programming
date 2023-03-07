#!/usr/bin/python3
def uppercase(str):
    i = 1
    n = len(str)
    if n == 0:
        return {0}
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            print("{}".format(chr(ord(ch) - 32)), end="" if i != n else "\n")
        else:
            print("{}".format(ch), end="" if i != n else "\n")
        i += 1
