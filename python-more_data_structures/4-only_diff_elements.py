#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    s1 = list(set_1)
    s2 = list(set_2)
    for num1 in s1:
        for num2 in s2:
            if num1 == num2:
                s1.remove(num1)
                s2.remove(num2)

    retorno = s1 + s2
    retorno = set(retorno)

    return retorno
