#!/usr/bin/python3
def uniq_add(my_list=[]):
    suma = set(my_list)
    resultado = 0
    for num in suma:
        resultado += num
    
    return resultado
