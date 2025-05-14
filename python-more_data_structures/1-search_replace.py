#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy = []
    for num in my_list:
        copy.append(num)
    for i, num in enumerate(copy):
        if num == search:
            copy[i] = replace
    return copy
