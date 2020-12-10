#!/usr/bin/env python3

import os
import sys

def readFile(input_file):
    a = [int(i.strip()) for i in open(input_file, 'r').readlines()]
    return a

def main(arguments):
    adapters, differences, j = readFile('input.txt'), [0,0,0], 0
    adapters.sort()
    for i,a in enumerate(adapters):
        print(j, a, i)
        if a - j <= 3:
            differences[a-j-1] += 1
            j = a
        if i == len(adapters)-1:
            differences[2] += 1

    print(differences[0] * differences[2])

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
