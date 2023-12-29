#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    temp = ""
    for ch in str:
        if i != n:
            temp += ch
        i += 1
    return (temp)
