#!/usr/bin/python3
if __name__ == "__main__":
    import sys, hidden_4
    args = dir(hidden_4)
    for i in args:
        if i[0] != '_':
            print(i)
