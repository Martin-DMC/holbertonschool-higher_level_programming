#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_list = []
    for num1 in set_1:
        for num2 in set_2:
            if num1 == num2:
                new_list.append(num1)
    new_list = set(new_list)

    return new_list
