#!/usr/bin/python3
def p(c=65): print(chr(c), end='\n' if c==90 else '') or (c<90 and p(c+1))
p()
