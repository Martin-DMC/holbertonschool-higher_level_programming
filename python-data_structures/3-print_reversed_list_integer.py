def print_reversed_list_integer(my_list=[]):
    size = len(my_list) - 1
    while size >= 0:
        valor = int(my_list[size])
        print("{:d}".format(valor))
        size -= 1
