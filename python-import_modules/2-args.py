#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = (len(argv) - 1)

    if argc == 0:
        print(f"{argc} argument.")
    else:
        print(f"{argc} arguments:")
        i = 1
        for arg in argv:
            if arg[0] == '.':
                continue
            else:
                print(f"{i}: {arg}")
                i += 1