#!/usr/bin/env python3

import os
import sys

def readFile(input_file):
    f, a = open(input_file, 'r'), []
    for num in f.readlines():
        a.append(int(num.strip()))
    return a

def solve(val, c):

    for i in range(len(c)):
        for k in range(i+1):
            sub_set = c[k:i+1]
            if sum(sub_set) == val:
                sub_set.sort()
                return(sub_set[0]+sub_set[-1])

def main(arguments):
    content = readFile('input.txt')

    ANSWER_FROM_PART_ONE = 507622668
    answer = solve(ANSWER_FROM_PART_ONE, content)
    print(answer)    

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
