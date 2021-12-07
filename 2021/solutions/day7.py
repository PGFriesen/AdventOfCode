#!/usr/bin/env python3

import os
import sys
import numpy as np
from dotmap import DotMap
from parse import parse


def part_one(crabs):
    crabs.sort()

    mid = int(len(crabs)/2)
    pos = crabs[mid]
    if len(crabs) % 2 == 0:
        pos = (pos + crabs[mid-1])/2

    cost = 0
    for crab in crabs:
        cost += abs(pos - crab)

    print("Part 1 - Total Fuel Cost: %d" % (int(cost)))


def part_two(crabs):
    pos = np.floor(np.mean(crabs))

    cost = 0
    for crab in crabs:
        cost += (pow(abs(pos - crab), 2) + abs(pos - crab)) / 2

    print("Part 2 - Total Fuel Cost: %d" % (int(cost)))


def main(arguments):
    input_file = "../inputs/input7.txt"
    # input_file = "sample.txt"  # using this file for the test use case

    with open(input_file, 'r') as f:
        contents = f.read()

    data = contents.split(',')
    crabs = [int(crab) for crab in data]


    part_one(crabs.copy())
    part_two(crabs.copy())


if __name__ == '__main__':
    sys.exit(main(sys.argv[0:]))
