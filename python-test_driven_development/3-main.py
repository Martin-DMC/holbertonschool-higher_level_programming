#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)

try:
    say_my_name()
except Exception as e:
    print(e)

try:
    say_my_name("White", None)
except Exception as e:
    print(e)