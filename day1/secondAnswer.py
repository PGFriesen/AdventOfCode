#!/usr/bin/env python3

import os
import sys

def readFile(input_file):
    f = open(input_file, 'r')
    return f.readlines()


def function1():
    print("function placeholder")


def function2():
    print("function placeholder")


def main(arguments):
    c = readFile('firstInput.txt')
    for i in range(0, len(c)):
        c[i] = int(c[i].strip())

    c.sort()
    print(c)
    for i in c:
        f = c[0]
        s = i
        t = c[-1]

        while (f < t):
            if (f+s+t == 2020):
                print("Answer:")
                print(str(f*s*t))
                print(f,s,t)
                quit()

            elif (f+s+t > 2020):
                t = c[c.index(t)-1]

            else:
                f = c[c.index(f)+1]

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
