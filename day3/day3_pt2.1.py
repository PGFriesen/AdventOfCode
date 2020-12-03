#!/usr/bin/env python3

import os
import sys
import math

def readFile(input_file):
    f = open(input_file, 'r')
    return f.readlines()

def solve(hill, trees, slopes):
    for index in range(1, len(hill)):
        row = hill[index].strip()
        for i,coords in enumerate(slopes):
            if (index % coords[1] == 0) and (row[int((index*coords[0]/coords[1]) % len(row))]=='#'):
                trees[i] += 1

    print(math.prod(trees))

def main(arguments):
    content = readFile('input.txt')
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    trees = [0,0,0,0,0]
    solve(content, trees, slopes)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
