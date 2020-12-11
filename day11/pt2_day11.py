#!/usr/bin/env python3

import os
import sys

def readFile(input_file):
    with open(input_file,'r') as f:
        a = [i.strip(' \n').replace('\n','') for i in f.readlines()]
    return a

def checkSeat(m, x, y, v):
    s, moved = countSeen(m, x, y), False
    if m[x][y] == 'L' and s == 0:          
        v[x][y] = 1
        moved = True
    elif m[x][y] == '#' and s >= 5:
        v[x][y] = 2
        moved = True    
    else:
        v[x][y] = 0
    return moved

def countSeen(m,x,y):
    seen = 0
    exists = ['']*9

    # Check all rows behind up to (Covered NE, N, NW)
    for i in range(x-1,-1,-1):
        diff = x-i
        #(NW)
        if (y-diff) >= 0:
            if m[i][y-diff] == '#' and exists[0] != False:
                exists[0] = True
            elif m[i][y-diff] == 'L' and exists[0] != True:
                exists[0] = False
        #(NE)
        if (y+diff) < len(m[x]): 
            if m[i][y+diff] == '#' and exists[2] != False:
                exists[2] = True
            elif m[i][y+diff] == 'L' and exists[2] != True:
                exists[2] = False
        # N
        if m[i][y] == '#' and exists[1] != False:
            exists[1] = True
        elif m[i][y] == 'L' and exists[1] != True:
            exists[1] = False

    if x < len(m)-1:
        # Check all rows after from (Covered SE, S, SW)
        for i in range(x+1, len(m)):      
            diff = i-x
            #(SW)
            if (y-diff) >= 0:
                if m[i][y-diff] == '#' and exists[6] != False:
                    exists[6] = True
                elif m[i][y-diff] == 'L' and exists[6] != True:
                    exists[6] = False
            #(SE)
            if (y+diff) < len(m[x]): 
                if m[i][y+diff] == '#' and exists[8] != False:
                    exists[8] = True
                elif m[i][y+diff] == 'L' and exists[8] != True:
                    exists[8] = False
    
            # S
            if m[i][y] == '#' and exists[7] != False:
                exists[7] = True
            elif m[i][y] == 'L' and exists[7] != True:
                exists[7] = False

    if y < len(m[x])-1:
        # Check all to the right (Covered W)
        for i in range(y+1, len(m[x])):
            if m[x][i] == '#' and exists[5] != False:
                exists[5] = True
            elif m[x][i] == 'L' and exists[5] != True:
                exists[5] = False
    
    # Check all to the left (Covered E)
    for i in range(y-1,-1,-1):
        if m[x][i] == '#' and exists[3] != False:
            exists[3] = True
        elif m[x][i] == 'L' and exists[3] != True:
            exists[3] = False

    for i in exists:
        if i == True:
            seen += 1

    return seen

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
        arr = ['0']*(len(row))
        mappings.append(arr)

    i = 0
    while changed == True:
        changed = False
        for r, row in enumerate(seats):
            for c, column in enumerate(row):
                if checkSeat(seats, r, c, mappings) == True:
                    changed = True
        i += 1
        print(i)
        for z in seats:
            print(z)
        if changed:
            switchSeats(seats, mappings)

    for row in seats:
        seated += row.count('#')

    print(seated)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
