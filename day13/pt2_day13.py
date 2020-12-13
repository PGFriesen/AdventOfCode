#!/usr/bin/env python3

import os
import sys

def readFile(input_file):
    with open(input_file,'r') as f:
        a = [i.strip(' \n') for i in f.readlines()]
    return a

def findTimestamp(busses):
    t, dt, i = 1, 1, 0
    while i < len(busses):
        while busses[i] == 'x':
            i += 1
        if ((t+i) % int(busses[i])) == 0:
            dt *= int(busses[i])
            i += 1
            print("i={}, dt={}, t={}".format(i-1,dt,t))
        t += dt
    
def main(arguments):
    content = readFile('input.txt')
    b = content[1].split(',')
    findTimestamp(b)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
