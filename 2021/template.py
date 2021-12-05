#!/usr/bin/env python3

import os
import sys
from dotmap import DotMap
from parse import parse


def part_one(input_list):
    print("Answer to Part 1: ")


def part_two(input_list):
    print("Answer to Part 2: ")


def load(data):
    return [
        DotMap(parse("{val:w}", line).named)
        for line in data.split("\n")
    ]


def main(arguments):
    input_file = "inputs/sample.txt"
    # input_file = "sample.txt"  # using this file for the test use case

    with open(input_file, 'r') as f:
        contents = f.read()

    data = load(contents)
    for line in data:
        print(line)

    part_one(data.copy())
    part_two(data.copy())


if __name__ == '__main__':
    sys.exit(main(sys.argv[0:]))
