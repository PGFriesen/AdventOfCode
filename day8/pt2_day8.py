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

def checkInstructions(instr, index, code, swap):
    instructions, i, accumulator, seen, n = [], 0,0, [], 0
    for ind, item in enumerate(instr):
        if ind == index and code != 'acc':
            instructions.append(item.replace(code, swap))
        else:
            instructions.append(item)

    while n <= (len(instr)*5):
        n += 1
        if i == len(instructions):
            print(accumulator)
            accumulator = 1000001
            return True
        code = instructions[i][0:3]
        seen.append(i)
        if code == 'jmp':
            i += getValue(instructions[i][4:])
        elif code == 'nop':
            i += 1
        else:
            accumulator += getValue(instructions[i][4:])
            i += 1
    return False

def main(arguments):
    instr = readFile('input.txt')
    for i,v in enumerate(instr):
        code = instr[i][0:3]
        if code == 'jmp':
            swap = 'nop'
        elif code == 'nop':
            swap = 'jmp'

        if checkInstructions(instr, i, code, swap) == True:
            print('done')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
