#!/usr/bin/env python3

import os
import sys


def read_file(input_file):
    with open(input_file,'r') as f:
        lines = f.readlines()
        input_list = [i.strip(' \n') for i in lines]
    return input_list


def part_one(input_list):
    gamma, epsilon = find_most_least_common(input_list)
    print("Part 1 - Power Consumption: %d" % (int(gamma,2) * int(epsilon,2)))


def part_two(input_list):
    # Calculate Oxygen Generator Rating
    iterate, bit, remaining = input_list.copy(), 0, []
    while len(iterate) > 1:
        most, least = find_most_least_common(iterate)
        for number in iterate:
            if number[bit] == most[bit]:
                remaining.append(number)

        iterate = remaining.copy()
        remaining.clear()

        bit += 1
    oxygen = iterate[0]

    # Calculate C02 Scrubber rating
    iterate, bit, remaining = input_list.copy(), 0, []
    while len(iterate) > 1:
        most, least = find_most_least_common(iterate)
        for number in iterate:
            if number[bit] == least[bit]:
                remaining.append(number)

        iterate = remaining.copy()
        remaining.clear()

        bit += 1
    carbon = iterate[0]

    # Multiply to get life support rating
    print("Part 2 - Life Support Rating: %d" % (int(carbon, 2) * int(oxygen, 2)))


def find_most_least_common(bit_list):
    g, e = "", ""

    for col in range(len(bit_list[0])):
        zeros, ones = 0, 0
        for row, number in enumerate(bit_list):
            if bit_list[row][col] == '0':
                zeros += 1
            else:
                ones += 1

        g = (g + '1') if ones >= zeros else (g + '0')
        e = (e + '0') if ones >= zeros else (e + '1')

    return g, e


def main(arguments):
    input_file = "inputs/input3.txt"
    # input_file = "inputs/sample.txt" # using this file for the test use case

    input_values = read_file(input_file)
    part_one(input_values)
    part_two(input_values)


if __name__ == '__main__':
    sys.exit(main(sys.argv[0:]))
