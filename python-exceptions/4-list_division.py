#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    if not isinstance(my_list_1, list) or my_list_1 is None:
        raise TypeError("my_list_1 debe ser una lista y no puede ser None")
    if not isinstance(my_list_2, list) or my_list_2 is None:
        raise TypeError("my_list_2 debe ser una lista y no puede ser None")
    if list_length < 0:
        raise ValueError("list_length no puede ser menor que 0")
    i = 0
    num = 0
    new_list = []
    max_length = max(len(my_list_1), len(my_list_2))
    while i < list_length and i < max_length:
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
