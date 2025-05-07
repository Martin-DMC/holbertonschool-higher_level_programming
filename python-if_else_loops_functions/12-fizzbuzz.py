#!/usr/bin/python3
def fizzbuzz():
    mul_3 = "Fizz"
    mul_5 = "Buzz"
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            print(f"{mul_3}{mul_5}", end=" ")
        elif i % 5 == 0:
            if i == 100:
                print(f"{mul_5}", sep=" ", end="\n")
            print(f"{mul_5}", end=" ")
        elif i % 3 == 0:
            print(f"{mul_3}", end=" ")
        else:
            print(f"{i}", end=" ")
