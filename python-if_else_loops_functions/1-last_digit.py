#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digito = abs(number) % 10
if number < 0:
    frase = f"Last digit of {number} is -{digito} "
else:
    frase = f"Last digit of {number} is {digito} "
if digito > 5:
    frase = frase + "and is greater than 5"
elif digito < 6 and digito != 0:
    frase = frase + "and is less than 6 and not 0"
elif digito == 0:
    frase = frase + "and is 0"
print(frase)
