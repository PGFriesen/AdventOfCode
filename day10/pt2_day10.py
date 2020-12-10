#!/usr/bin/env python3

import os
import sys

def readFile(input_file):
    a = [int(i.strip()) for i in open(input_file, 'r').readlines()]
    return a

def main(arguments):
    adapters, configs = readFile('input.txt'), set()
    adapters.append(0)
    adapters.sort()
    removable = ['1']*len(adapters)
    for i in range(1,len(adapters)-1):
        removable[i] = '2' if adapters[i+1]-adapters[i-1] == 2 else '1'

    print(eval('*'.join(removable).replace('2*2*2','7')))
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
