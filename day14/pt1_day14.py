#!/usr/bin/env python3

import os
import sys

def readFile(input_file):
    with open(input_file,'r') as f:
        a = [i.strip(' \n') for i in f.readlines()]
    return a

def main(arguments):
    content = readFile('input.txt')
    mem = [] 
    for line in content:
        if line.startswith('mask'):
            mask = line.split()[2]
        else:
            loc, val, diff, res = int(line[4:line.index(']')]), format(int(line.split()[2]), 'b'), 36-len(str(format(int(line.split()[2]), 'b'))), ''
            while len(mem) < loc+1:
                mem.append('x')
            for i in range(diff):
                val = '0' + val
            
            for i,v in enumerate(val):
                if mask[i] != 'X':
                    res += mask[i]
                else:
                    res += val[i]
            mem[loc] = int(res,2) 
    a = 0
    for i in mem:
        if i != 'x':
            a += i
    print(a)
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
