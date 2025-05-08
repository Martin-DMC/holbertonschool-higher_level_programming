#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    res = 0
    for arg in range(1, len(argv)):
        arg_int = int(argv[arg])
        res += arg_int
    print(f"{res}")
