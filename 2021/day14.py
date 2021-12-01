#!/usr/bin/env python3

import os
import sys

def readFile(input_file):
    with open(input_file,'r') as f:
        content = f.readlines()
        strings = [i.strip(' \n') for i in content]
        try:
            integers = [int(i.strip(' \n')) for i in content]
        except:
            print("Input values are not integers")
            integers = strings
        
    return integers, strings

def partOne(arg):
    print("Answer to Part 1: ")

def partTwo(arg):
    print("Answer to Part 2: ")

def main(arguments):
    inputFile = "input" + arguments[0][3:arguments[0].index('.')] + ".txt"

    integer_input, string_input = readFile(inputFile)
    
    partOne(integer_input)
    partTwo(integer_input)
    
if __name__ == '__main__':
    sys.exit(main(sys.argv[0:]))
