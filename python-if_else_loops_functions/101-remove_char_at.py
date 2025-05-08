#!/usr/bin/python3
def remove_char_at(str, n):
    str_new = ""
    i = 0
    for letra in str:
        if not i == n:
            str_new += letra
            i += 1
        else:
            i += 1
            continue
    return str_new

