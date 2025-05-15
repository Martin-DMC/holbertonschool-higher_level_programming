#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    else:
        num = 0
        largo = len(roman_string)
        i = 0
        while i < largo:
            if roman_string[i] == "I":
                num += 1
                i += 1
            elif roman_string[i] == "V":
                if i > 0 and roman_string[i - 1] == "I":
                    num += 3
                    i += 1
                else:
                    num += 5
                    i += 1
            elif roman_string[i] == "X":
                if i > 0 and roman_string[i - 1] == "I":
                    num += 8
                    i += 1
                else:
                    num += 10
                    i += 1
            elif roman_string[i] == "L":
                if i > 0 and roman_string[i - 1] == "X":
                    num += 30
                    i += 1
                else:
                    num += 50
                    i += 1
            elif roman_string[i] == "C":
                if i > 0 and roman_string[i - 1] == "X":
                    num += 80
                    i += 1
                else:
                    num += 100
                    i += 1
            elif roman_string[i] == "D":
                if i > 0 and roman_string[i - 1] == "C":
                    num += 300
                    i += 1
                else:
                    num += 500
                    i += 1
            elif roman_string[i] == "M":
                if i > 0 and roman_string[i - 1] == "C":
                    num += 800
                    i += 1
                else:
                    num += 1000
                    i += 1
        return num
