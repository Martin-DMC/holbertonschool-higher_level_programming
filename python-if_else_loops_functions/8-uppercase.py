#!/usr/bin/python3
def uppercase(str):
    resultado = ""
    for letra in str:
        if ord('a') <= ord(letra) <= ord('z'):
            mayuscula_ascii = ord(letra) - (ord('a') - ord('A'))
            resultado += chr(mayuscula_ascii)
        else:
            resultado += letra
    print("{}".format(resultado))
