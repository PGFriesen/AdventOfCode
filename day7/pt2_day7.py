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

def countBags(rule_set, bag_key, number_of_bags):
    total = number_of_bags
    for bag, num in rule_set[bag_key].items():
        total += countBags(rule_set, bag, number_of_bags*num)
    return total

def main(arguments):
    rules, t = createKey(readFile('input.txt')), 0
    
    for bag, num in rules['shiny gold'].items():
        t += countBags(rules, bag, num)

    print(t)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
