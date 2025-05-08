#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = (len(argv) - 1)

    if argc == 0:
        print(f"{argc} arguments.")
    elif argc > 0:
        if argc == 1:
            print(f"{argc} argument:")
            print(f"1: {argv[1]}")
        else:
            i = 1
            print(f"{argc} arguments:")
            for arg in range(1, len(argv)):
                arg = argv[i]
                print(f"{i}: {arg}")
                i += 1