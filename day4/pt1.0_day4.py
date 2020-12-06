#!/usr/bin/env python3

import os
import sys

def main(arguments):
    with open('input.txt', 'r') as f, open('valid_passports.txt','w') as o:
        content = f.readlines()
        passport, valid, invalid, index = '', 0, 0, 0
    
        for i in range(len(content)):
            if i == len(content)-1 or content[i].strip() == '': # Hit a empty line telling us we are done with the last passport
                passport = content[index:i]
                if i == len(content)-1:
                    passport.append(content[i])
                entries = []
                opt = False
                for p in passport:
                    entries.extend(p.strip(' \n').split(' '))
                    if p.find('cid') > -1:
                        opt = True
                
                if ((len(entries) > 7) or (len(entries) == 7 and not opt)):
                    valid += 1
                    valid_string = entries[0]
                    for e in entries:
                        if e != entries[0]:
                            valid_string = valid_string + ' ' + e
                    print(valid_string)
                    o.write('{}\n'.format(valid_string))
                else:
                    invalid += 1

                index = i+1

        print(valid, invalid) 

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
