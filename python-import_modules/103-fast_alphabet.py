#!/usr/bin/python3
def p(c=65): print(chr(c), end=('','\n')[c==90]); c-90 and p(c+1)
p()
