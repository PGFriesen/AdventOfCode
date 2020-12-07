#!/usr/bin/env python3

import os
import sys
import re

def readFile(input_file):
    f = open(input_file, 'r')
    return f.readlines()


def createKey(list_of_rules):
    key = {}
    for line in list_of_rules:
        pair = line.strip().replace('.','').split('contain')
        
        k = pair[0][0:pair[0].index('bags')-1]
        key[k] = {}
        if line.find('no other bags') == -1:        
            for p in pair[1].strip().split(','):
                words = p.split()
                bag_type = words[1] + ' ' + words[2]
                key[k][bag_type] = int(words[0])
    return key       

def containsGoldBag(contents, keys):
    found = False
    for c in keys:
        if c == 'shiny gold':
            found = True
        else:
            if found != True:
                found = containsGoldBag(contents, contents[c].keys())

    return found

def main(arguments):
    content = readFile('input.txt')
    rules = createKey(content)


    tally = 0
    for rule, contents in rules.items():
        if containsGoldBag(rules, contents.keys()):
            tally += 1
    print(tally)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
