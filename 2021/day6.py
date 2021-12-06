#!/usr/bin/env python3

import os
import sys
from dotmap import DotMap
from parse import parse


def part_one(fishies):
    for i in range(80):
        new_fishies = 0
        for fish in range(len(fishies)):
            if fishies[fish] == 0:
                fishies[fish] = 6
                new_fishies += 1
            else:
                fishies[fish] -= 1

        for new in range(new_fishies):
            fishies.append(8)

    print(len(fishies))


def part_two(fishies):
    fishies_by_days = [fishies.count(i) for i in range(9)]

    spawn_more_fishies(256, fishies.copy())


def spawn_more_fishies(days, fishies):
    fishies_by_days = [fishies.count(i) for i in range(9)]

    for i in range(days):
        fishies_by_days = fishies_by_days[1:] + fishies_by_days[:1]
        fishies_by_days[6] += fishies_by_days[8]

    print(sum(fishies_by_days))


def main(arguments):
    input_file = "inputs/input6.txt"
    # input_file = "sample.txt"  # using this file for the test use case

    with open(input_file, 'r') as f:
        contents = f.read()

    data = contents.split(',')
    fishies = []
    for fish in data:
        fishies.append(int(fish))

    part_one(fishies.copy())
    part_two(fishies.copy())


if __name__ == '__main__':
    sys.exit(main(sys.argv[0:]))
