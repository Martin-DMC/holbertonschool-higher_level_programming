def roman_to_int(roman_string):
    if not roman_string:
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
                num += 5
                i += 1
            elif roman_string[i] == "X":
                num += 10
                i += 1
            elif roman_string[i] == "L":
                num += 50
                i += 1
            elif roman_string[i] == "C":
                num += 100
                i += 1
            elif roman_string[i] == "D":
                num += 500
                i += 1
            elif roman_string[i] == "M":
                num += 1000
                i += 1
        return num
