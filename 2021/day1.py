#!/usr/bin/env python3

import os
import sys

def readFile(input_file):
    with open(input_file,'r') as f:
        a = [int(i.strip(' \n')) for i in f.readlines()]
    return a

def main(arguments):
    content = readFile('input.txt')

    increase, decrease, previous = 0, 0, content[0]

    for index, item in enumerate(content):
        if item > previous:
            increase += 1
        previous = item

    print("Increases: %d" % (increase))

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
