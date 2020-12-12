#!/usr/bin/env python3

import os
import sys

def readFile(input_file):
    with open(input_file,'r') as f:
        a = [i.strip(' \n') for i in f.readlines()]
    return a

def function1():
    print("function placeholder")


def main(arguments):
    content = readFile('input.txt')


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
