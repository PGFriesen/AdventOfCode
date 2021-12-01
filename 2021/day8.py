#!/usr/bin/env python3

import os
import sys


"""
This function reads in from the input_file as a list where each line is a single item in the list

If all of the input values are numeric, then integers will contain....integers (otherwise integers and strings point to the same list)

Param: 
 - input_file: The filename to read from

Returns:
 - integers: The list of values. If the values from input_file are not numeric, this will simply be the same as strings
 - strings: The list of values as strings
"""
def readFile(input_file):
    with open(input_file,'r') as f:
        lines = f.readlines()
        strings = [i.strip(' \n') for i in lines]
        try:
            integers = [int(i.strip(' \n')) for i in lines]
        except:
            print("Input values are not integers")
            integers = strings
        
    return integers, strings

def partOne(arg):
    print("Answer to Part 1: ")

def partTwo(arg):
    print("Answer to Part 2: ")

"""
Main function to run the program. The file to read input from is determined by the name of the executable script.

Each day in December has it's own python script and it's own input file, so they are named accordingly - "day1.py" uses "input1.txt"
"""
def main(arguments):
    inputFile = "input" + arguments[0][3:arguments[0].index('.')] + ".txt"

    integer_input, string_input = readFile(inputFile)
    
    partOne(integer_input)
    partTwo(integer_input)
    
if __name__ == '__main__':
    sys.exit(main(sys.argv[0:]))
