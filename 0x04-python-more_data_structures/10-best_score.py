#!/usr/bin/python3
def best_score(a_dictionary):
    best = ""
    if a_dictionary == None:
        return None
    for i in a_dictionary:
        maxn = a_dictionary[i]
        best = i
        for k in a_dictionary:
            if a_dictionary[k] > maxn:
                best = k
                maxn = a_dictionary[k]
    return best
