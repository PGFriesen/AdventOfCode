#!/usr/bin/env python3

import os
import sys

def readFile(input_file):
    f = open(input_file, 'r')
    return f.readlines()


def function1():
    print("function placeholder")


def isValid(mini, maxi, key, pw):
    
    if ((pw[mini-1] == key or pw[maxi-1] == key) and pw[mini-1] != pw[maxi-1]):
        return True
    else:
        return False


def main(arguments):
    content = readFile('input.txt')

    count = 0
    for pw in content:
        e = pw.split(' ')
        minimum = e[0][0:e[0].index('-')]
        maximum = e[0][e[0].index('-')+1:]
        c = e[1][0]

        if (isValid(int(minimum), int(maximum), c, e[2])):
            count += 1

    print(count)
        
        

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
