#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = []
    for i in range(0, len(my_list)):
        copy.append(my_list[i])
    if idx < 0 or idx > len(copy):
        return copy
    else:
        for i in range(0, len(copy)):
            if i == idx:
                copy[i] = element
    return copy
