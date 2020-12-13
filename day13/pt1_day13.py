#!/usr/bin/env python3

import os
import sys

def readFile(input_file):
    with open(input_file,'r') as f:
        a = [i.strip(' \n') for i in f.readlines()]
    return a

def findEarliestDeparture(time, busses):
    departed, t = False, time
    while not departed:
        for bus in busses:
            if t % int(bus) == 0:
                departed = True
                print(bus, ((t-time)*int(bus)))
        t += 1

def main(arguments):
    content = readFile('input.txt')
    t = int(content[0])
    b = sorted(content[1].replace('x,','').split(','))
    findEarliestDeparture(t, b)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
