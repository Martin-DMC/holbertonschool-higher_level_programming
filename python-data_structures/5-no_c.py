def no_c(my_string):
    retorno = ""
    for char in my_string:
        if char == 'c' or char == 'C':
            continue
        else:
            retorno += char
    return retorno
