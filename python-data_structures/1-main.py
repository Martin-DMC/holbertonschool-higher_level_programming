#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
idx = 0
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
idx = 1
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
idx = 4
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))