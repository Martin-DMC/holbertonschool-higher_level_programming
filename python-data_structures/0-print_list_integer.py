def print_list_integer(my_list=[]):
    i = 0
    while i < len(my_list):
        valor = int(my_list[i])
        print("{:d}".format(valor))
        i += 1
