#!/usr/bin/env python3

import os
import sys

# Read content from file into a list of values
# If the values are all numeric, then "integers" will be a list of integers and strings are just the string equivelants
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
    increase, previous = 0, arg[0]
    for index, item in enumerate(arg):
        if item > previous:
            increase += 1
        previous = item

    print("Part 1: %d increases" % (increase))

def partTwo(arg):
    increase, previousGroup = 0, [0,0,9999999999]
    for i in range(2, len(arg)):
        currentGroup = [arg[i-k] for k in range(3)]
        if sum(currentGroup) > sum(previousGroup):
            increase += 1

        previousGroup = currentGroup

    print("Part 2: %d increases" % (increase))

def main(arguments):
    inputFile = "input1.txt"
    if len(arguments) >= 1:
        inputFile = arguments[0]
    integer_input, string_input = readFile(inputFile)
    
    partOne(integer_input)
    partTwo(integer_input)
    
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
