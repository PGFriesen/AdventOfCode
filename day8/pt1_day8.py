#!/usr/bin/env python3

import os
import sys

def readFile(input_file):
    a = []
    with open(input_file,'r') as f:
        arr = f.readlines()
        for line in arr:
            a.append(line.strip(' \n'))
    return a

def getValue(i):
    num = int(i[1:])
    if i[0] == '-':
        num *= -1
    return num

    
def main(arguments):
    instructions,i,accumulator,seen = readFile('input.txt'),0,0,[]
    
    while i not in seen:
        code = instructions[i][0:3]
        seen.append(i)
        if code == 'jmp':
            i += getValue(instructions[i][4:])
        elif code == 'acc':
            accumulator += getValue(instructions[i][4:])
            i += 1
        else:
            i += 1
        print(accumulator)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
