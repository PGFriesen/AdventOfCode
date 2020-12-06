#!/usr/bin/env python3

import os
import sys
import re

def validateAttr(key, val):
    valid = True
    try:
        if key == 'byr':
            if int(val) < 1920 or int(val) > 2002:
                valid = False
        elif key == 'iyr':
            if int(val) < 2010 or int(val) > 2020:
                valid = False
        elif key == 'eyr':
            if int(val) < 2020 or int(val) > 2030:
                valid = False
        elif key == 'hgt':
            if val[-2:] == 'cm':
                if (int(val[0:val.index('cm')]) > 193) or (int(val[0:val.index('cm')]) < 150):
                    valid = False
            elif val[-2:] == 'in':
                if int(val[0:val.index('in')]) > 76 or int(val[0:val.index('in')]) < 59:
                    valid = False
            else:
                valid = False
        elif key == 'hcl':
            if re.search("^\#[a-f0-9]{6}$", val) is None:
                valid = False
        elif key == 'ecl':
            colors = ['amb','blu','brn','gry','grn','hzl','oth']
            if val not in colors:
                valid = False

        elif key == 'pid':
            if re.search("^[0-9]{8}[0-9]{1}$", val) is None:
                valid = False
    except e:
        valid = False

    return valid

def main(arguments):
    with open('valid_passports.txt', 'r') as f:
        content = f.readlines()
        valid, invalid = 0, 0
    
        for index, passport in enumerate(content):
            testString = ''
            is_valid = True
            p_list = passport.strip(' \n').split(' ')
            for e in p_list:
                pair = e.split(':')
                if validateAttr(pair[0],pair[1]) == False:
                    testString += '{}:{} '.format(pair[0],pair[1])
                    is_valid = False
                    
            if is_valid:
                valid += 1
            else:
                print(p_list, testString, invalid)
                invalid += 1

        print(valid, invalid)
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
