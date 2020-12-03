#!/usr/bin/env python3

import os
import sys

def readFile(input_file):
    f = open(input_file, 'r')
    return f.readlines()

def numberOfTreesInSlope(dx, dy, hill):
    x,trees = 0,0
    for i in range(0,len(hill), dy):
        if hill[i][x] == '#':
            trees += 1
        x = ( (x+dx) % len(hill[i].strip()) )
       
    print(trees, dx, dy)
    return trees

def main(arguments):
    content = readFile('input.txt')
    slopes = ((1,1),(3,1),(5,1),(7,1),(1,2))    

    total_trees = numberOfTreesInSlope(1, 1, content)
    for index in range(1,len(slopes)):
        total_trees *= numberOfTreesInSlope(slopes[index][0], slopes[index][1], content)
        
    print(total_trees)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
