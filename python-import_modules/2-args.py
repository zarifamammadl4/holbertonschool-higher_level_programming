#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # script ismi hariç argümanlar
    argc = len(argv)

    if argc == 0:
        print("0 arguments.")
    else:
        word = "argument" if argc == 1 else "arguments"
        print("{} {}:".format(argc, word))
        for i, arg in enumerate(argv, 1):
            print("{}: {}".format(i, arg))
