#!/usr/bin/env python3

import os
import sys

def readFile(input_file):
    f = open(input_file, 'r')
    return f.readlines()


def move(sled, i):
    sled[1] += 1
    sled[0] = (sled[0]+3) % (len(i.strip()))
    isTree(sled, i[sled[0]])


def isTree(sled, spot):
    if spot == '#':
        sled[2] += 1
    else:
        sled[3] += 1


def main(arguments):
    content = readFile('input.txt')
    
    sled = [0,0,0,0]
    for index in range(len(content)-1):
        move(sled, content[index+1].strip())

    print(sled)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
