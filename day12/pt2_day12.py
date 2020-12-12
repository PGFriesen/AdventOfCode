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

def rotateWaypoint(waypoint, instruction, compass):
    cpy, r = waypoint.copy(), False
    if instruction[0] == 'L':
        cpy.reverse()
        r = True
    for i in range(0, int(int(instruction[1:])/90)):
        w = [cpy[-1]]
        w.extend(cpy[0:len(cpy)-1])
        cpy = w
    
    if r:
        cpy.reverse()

    return cpy

def main(arguments):
    content, compass, coords = readFile('input.txt'), ['North','East','South','West'], [0,0,0,0]
    facing = compass[1]
    wp = [1,10,0,0]

    for i in content:       # i = instruction
        if i[0] in ['N','S','E','W']:
            move(wp, i)
        elif i[0] == 'L' or i[0] == 'R':
            wp = rotateWaypoint(wp, i, compass)
        else:
            for k in range(int(i[1:])):
                for index, val in enumerate(wp):
                    move(coords, '{}{}'.format(compass[index][0],val))

    ending = coords.copy()
    print(ending)
    
    print(abs(ending[1]-ending[3])+(abs(ending[0]-ending[2])))
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
