#!/usr/bin/env python3

import os
import sys

def readFile(input_file):
    with open(input_file,'r') as f:
        a = [i.strip(' \n') for i in f.readlines()]
    return a

def move(c, i):
    val = int(i[1:])
    if i[0] == 'N':
        c[0] = c[0] + val
    elif i[0] == 'E':
        c[1] = c[1] + val
    elif i[0] == 'S':
        c[2] = c[2] + val
    else:
        c[3] = c[3] + val

def rotate(f, c, i):
    if i[0] == 'L':
        flip = c.copy()
        flip.reverse()
        return flip[(flip.index(f)+int(int(i[1:])/90)) % len(c)]
    else:
        return c[(c.index(f)+int(int(i[1:])/90)) % len(c)]

def main(arguments):
    content, compass, coords = readFile('input.txt'), ['North','East','South','West'], [0,0,0,0]
    facing = compass[1]     # Start facing East
    
    starting = coords.copy()
    starting.append(facing)
    print(starting)
    for i in content:       # i = instruction
        if i[0] in ['N','S','E','W']:
            move(coords, i)
        elif i[0] == 'L' or i[0] == 'R':
            facing = rotate(facing, compass, i)
        else:
            move(coords, i.replace('F', facing[0]))

    ending = coords.copy()
    ending.append(facing)
    print(ending)
    
    print(abs(ending[1]-ending[3])+(abs(ending[0]-ending[2])))
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
