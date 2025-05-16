#!/usr/bin/python3
def safe_print_division(a, b):
    resultado = None
    try:
        resultado = (a / b)
    except ZeroDivisionError:
        None
    finally:
        if resultado is not None:
            print("Inside result: {:.2f}".format(resultado))
        else:
            print("Inside result: None")
        return resultado
