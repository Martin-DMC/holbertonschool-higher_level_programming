#!/usr/bin/python3
import sys

if __name__ == "__main__":
    variable_load_5_modulo = sys.modules.get('variable_load_5')
    if variable_load_5_modulo is not None:
        variable = variable_load_5_modulo.a
        print(variable)