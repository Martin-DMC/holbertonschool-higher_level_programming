#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    while True:
        try:
            if i < x:
                print(f"{my_list[i]}", end="")
                i += 1
            else:
                break
        except IndexError:
            break
    print("")
    return i
