#!/usr/bin/env python3

import os
import sys

def readFile(input_file):
    f, a = open(input_file, 'r'), []
    for num in f.readlines():
        a.append(int(num.strip()))
    return a

# Given a list of integers, start at the 26th and check if each number is the sum of two numbers in the last 25
def solve(c):
    for i in range(25,len(c)):                          # Start at 26th number
        adds_up, last_section = False, c[i-25:i]        # assume it does not equal the sum of two previous
        
        for outer, k in enumerate(last_section):        # check each number
            for inner, v in enumerate(last_section):    # against each number
                if (outer != inner) and (k+v == c[i]):  # and if they add up we keep moving forward
                    adds_up = True
        
        if adds_up == False:                            # if they do not add up, we have our answer
            return c[i]

def main(arguments):
    content, nums = readFile('input.txt'), []

    answer = solve(content)
    print(answer)    

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
