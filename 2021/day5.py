#!/usr/bin/env python3

import os
import sys


def solve(input_list):
    grid, row = [], [0] * 1000  # Grid is 1000 x 1000 (Just looked at input and saw that there are no 4 digit coords)
    for i in range(1000):
        grid.append(row.copy())

    annotate_grid(grid, input_list)

    # "Hey Lana"
    # "Lana....Lana....Lana"
    # "....."
    # "LAAAAAAAAAAANNNNNNNNAAAAAAAAAAAAAAA"
    # "WHAT?"
    # "....."
    # "..........dangaaaaaa zone"
    danger_zones = 0

    for row in grid:
        r = row.count(0)
        r += row.count(1)
        danger_zones += (len(row) - r)

    print("\nPart 2 - Number of Danger Zones: %d" % (danger_zones))


def annotate_grid(grid, vents):
    for vent_coordinates in vents:
        x1, y1 = vent_coordinates[0:vent_coordinates.find("->")].strip().split(',')
        x2, y2 = vent_coordinates[vent_coordinates.find("->"):].replace("->", "").strip().split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        dX, dY = x2 - x1, y2 - y1

        # Horizontal and Vertical
        if is_horizontal_or_vertical(x1, y1, x2, y2):
            if dY == 0:
                for x in range(x1, x2+int(dX/abs(dX)), int(dX/abs(dX))):
                    grid[y1][x] += 1
            elif dX == 0:
                for y in range(y1, y2+int(dY/abs(dY)), int(dY/abs(dY))):
                    grid[y][x1] += 1

        # Part 2: Diagonal lines, comment this else block out to just get part 1
        else:
            for n in range(int(abs(dX))+1):
                grid[y1+(n*int(dY/abs(dY)))][x1+(n*int(dX/abs(dX)))] += 1


def is_horizontal_or_vertical(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        return True
    return False


def print_grid(grid):
    # Mostly for debugging with test case
    print("", end='   ')
    for i in range(len(grid[0])):
        print(i, end=', ')
    print()

    for row_num, row in enumerate(grid):
        print(row_num, row)
    print('\n')


def read_file(input_file):
    # Read and clean input from provided file and return a list
    with open(input_file, 'r') as f:
        lines = f.readlines()
        input_list = [i.strip(' \n') for i in lines]

    return input_list


def main(arguments):
    input_file = "inputs/input5.txt"
    #input_file = "sample.txt"  # using this file for the test use case

    input_list = read_file(input_file)
    solve(input_list)


if __name__ == '__main__':
    sys.exit(main(sys.argv[0:]))
