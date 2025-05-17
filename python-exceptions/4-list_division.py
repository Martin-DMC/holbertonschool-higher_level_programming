#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    num = 0
    new_list = []
    while i < list_length:
        try:
            a = int(my_list_1[i])
            b = int(my_list_2[i])
            num = a / b
            num = round(num, 1)
        except (TypeError, ValueError):
            num = 0
            print("wrong type")
        except IndexError:
            num = 0
            print("out of range")
        except ZeroDivisionError:
            num = 0
            print("division by 0")
        finally:
            new_list.append(num)
            i += 1
    return new_list
