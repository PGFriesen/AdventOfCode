#!/usr/bin/env python3

import os
import sys

def readFile(input_file):
    f = open(input_file, 'r')
    return f.readlines()


def function1():
    print("function placeholder")


def main(arguments):
    content = readFile('input.txt')

    list_seat_ids, max_id, min_id = [], 0, 1023
    for line in content:
        line = line.strip(' \n')
        
        f, b, l, r = 0, 128, 0, 8
        for i in range(len(line)):
            letter = line[i]
             
            if i == 6:
                if letter == 'F':
                    row = f
                else:
                    row = b-1

            elif i == 9:
                if letter == 'L':
                    seat = l
                else:
                    seat = r-1
            elif letter == 'F':
                b = b - ((b-f)/2)
            elif letter == 'B':
                f = f + ((b-f)/2)
            elif letter == 'R':
                l = l + ((r-l)/2)
            elif letter == 'L':
                r = r - ((r-l)/2)

        seat_id = (row * 8) + seat
        if row != 0 and row != 127:
            list_seat_ids.append(seat_id)
        
        if seat_id > max_id:
            max_id = seat_id
            
    for i in range(28,843):
        if i not in list_seat_ids and i+1 in list_seat_ids and i-1 in list_seat_ids:
            print(i)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
