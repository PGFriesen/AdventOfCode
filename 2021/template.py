#!/usr/bin/env python3

import os
import sys


def part_one(arg):
    print("Answer to Part 1: ")


def part_two(arg):
    print("Answer to Part 2: ")


def read_file(input_file):
    # Read and clean input from provided file and return a list
    with open(input_file, 'r') as f:
        lines = f.readlines()
        input_list = [i.strip(' \n') for i in lines]

    return input_list


def main(arguments):
    input_file = "input.txt"
    # input_file = "sample.txt" # using this file for the test use case

    input_list = read_file(input_file)

    part_one(input_list)
    part_two(input_list)


if __name__ == '__main__':
    sys.exit(main(sys.argv[0:]))
