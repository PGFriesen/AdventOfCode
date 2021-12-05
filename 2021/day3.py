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
    input_file = "testInput.txt"
    with open(input_file,'r') as f:
        lines = f.readlines()
        input_list = [i.strip(' \n') for i in lines]
        
    return input_list

def partOne(arg):
    
    str_gamma, str_epsilon = "",""
    for bit in range(len(arg[0])):
        z, o = 0,0

        # this loop counts the number of 0's and 1's in the given column
        for row, value in enumerate(arg):
            if arg[row][bit] == '1':
                o += 1
            else:
                z += 1

        # determine the most common bits (gamma) and least common bits (epsilon)
        if o >= z:
            str_gamma += '1'
            str_epsilon += '0'
        elif o < z:
            str_gamma += '0'
            str_epsilon += '1'

    print("\nPart 1:\ngamma = %s (%d)\nepsilon = %s (%d)\nPower Consumption: %d\n\n" % (str_gamma, int(str_gamma, 2), str_epsilon, int(str_epsilon, 2), int(str_epsilon,2) * int(str_gamma, 2)))

    return str_gamma, str_epsilon

def partTwo(arg):

    gamma, epsilon = partOne(arg)
    gen_ratings, scr_ratings = arg.copy(),arg.copy()
    g,s = "",""

    print("gamma=%s" % (gamma))
    for i in range(len(gamma)):
        found = 0
        substr = gamma[0:i+1]
        print("substring=%s" % (substr))
        for val in arg:
            if val[0:i+1] == substr:
                print(val)
                found += 1
        

    print("\n\nepsilon=%s" % (epsilon))
    for i in range(len(epsilon)):
        found = 0
        substr = epsilon[0:i+1]

        for val in arg:
            if val[0:i+1] == substr:
                found += 1

    """
    #for index, bit in enumerate(gamma):
    index = 0
    while(len(gen_ratings) > 1):    
        bit = gamma[index]
        
        for value in arg:
            if len(gen_ratings) > 1 and value in gen_ratings and value[index] != gamma[index]:
                gen_ratings.remove(value)
        #print(gamma)
        #print(index, bit)
        for val in gen_ratings:
            print(val)

        index += 1          
        #print("\n\n")

    index = 0
    while(len(scr_ratings) > 1):
        bit = epsilon[index]

        for value in arg:
            if len(scr_ratings) > 1 and value in scr_ratings and value[index] != epsilon[index]:
                scr_ratings.remove(value)
        #print(epsilon)
        #print(index, bit)
        for val in scr_ratings:
            print(val)
        #index += 1
        print("\n\n")
        """
    print("Answer to Part 2: ")

"""
Main function to run the program. The file to read input from is determined by the name of the executable script.

Each day in December has it's own python script and it's own input file, so they are named accordingly - "day1.py" uses "input1.txt"
"""
def main(arguments):
    inputFile = "input" + arguments[0][3:arguments[0].index('.')] + ".txt"

    input_values = readFile(inputFile)
    
    partTwo(input_values)
    
if __name__ == '__main__':
    sys.exit(main(sys.argv[0:]))
