#!/usr/bin/env python3

import os
import sys

def readFile(input_file):
    f = open(input_file, 'r')
    return f.readlines()

def main(arguments):
    content = readFile('input.txt')
    
    approved_by_group = set()
    groups_answers = []
    tally = 0
    for i, line in enumerate(content):
        set_of_answers = set()
        line = line.strip(' \n')

        if line == '':
            approved_by_group = groups_answers[0]
            for index in range(len(groups_answers)):
                approved_by_group = approved_by_group.intersection(groups_answers[index])
            tally += len(approved_by_group)
            groups_answers = [] 
        
        elif i == len(content)-1:
            for letter in line:
                set_of_answers.add(letter)
            groups_answers.append(set_of_answers)

            for answers in groups_answers:
                approved_by_group = approved_by_group.intersection(answers)
            tally += len(approved_by_group)

        else:
            for letter in line:
                set_of_answers.add(letter)
            groups_answers.append(set_of_answers)

    print(tally)
        

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
