#!/usr/bin/env python3

import os
import sys

def readFile(input_file):
    with open(input_file,'r') as f:
        a = [i.strip(' \n').replace('\n','') for i in f.readlines()]
    return a

def checkSeat(m, x, y, v):
    a, moved = countAdjacents(m, x, y), False
    if m[x][y] == 'L' and a == 0:          
        v[x][y] = 1
        moved = True
    elif m[x][y] == '#' and a >= 4:
        v[x][y] = 2
        moved = True    
    else:
        v[x][y] = 0
    return moved

def countAdjacents(m, x, y):
    adj = 0
    for i in range(-1, 2, 1):
        for k in range(-1, 2, 1):
            if (x+i >= 0) and (x+i < len(m)) and (y+k >= 0) and (y+k < len(m[x])):
                if i == 0 and k == 0:
                    continue
                else:
                    if m[x+i][y+k] == '#':
                        adj += 1
    return adj

def switchSeats(m, v):
    for r, row in enumerate(m):
        for c, col in enumerate(row):
            if v[r][c] == 1:
                m[r] = m[r][0:c] + m[r][c:].replace('L','#',1)
            elif v[r][c] == 2:
                m[r] = m[r][0:c] + m[r][c:].replace('#','L',1)

def main(arguments):
    seats, changed, seated, mappings = readFile('input.txt'), True, 0, []
    for row in seats:
        arr = ['0']*len(row)
        mappings.append(arr)

    i = 0
    while changed == True:
        changed = False
        for r, row in enumerate(seats):
            for c, column in enumerate(row):
                if checkSeat(seats, r, c, mappings) == True:
                    changed = True
        i += 1
        if changed:
            switchSeats(seats, mappings)

    for row in seats:
        seated += row.count('#')

    print(seated)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
