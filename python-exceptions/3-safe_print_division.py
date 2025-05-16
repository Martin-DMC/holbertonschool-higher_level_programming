#!/usr/bin/python3
def safe_print_division(a, b):
    resultado = None
    try:
        resultado = (a / b)
    except ZeroDivisionError:
        return None
    finally:
        if resultado is not None:
            print("Inside result: {:.1f}".format(resultado))
        else:
            print("Inside result: None")
        return resultado
