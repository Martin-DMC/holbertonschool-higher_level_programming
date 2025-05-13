#!/usr/bin/python3
def max_integer(my_list=[]):
    #res = max(my_list)
    maximus = 0
    for num in my_list:
        if num > maximus:
            maximus = num
    return maximus
