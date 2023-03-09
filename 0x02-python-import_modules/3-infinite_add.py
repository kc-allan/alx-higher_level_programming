#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    _sum = 0
    if n == 1:
        print(0)
    else:
        for i in range(1, n, 1):
            _sum += int(argv[i])
        print(_sum)
