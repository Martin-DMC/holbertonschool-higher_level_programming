#!/usr/bin/python3
def element_at(my_list, idx):
    valor = int(my_list[0])
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        for i in my_list:
            if i == idx:
                valor = int(my_list[i])
        return valor
