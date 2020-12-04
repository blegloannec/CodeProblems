#!/usr/bin/env python3

import sys, re

I = [L.strip() for L in sys.stdin.readlines()]
I.append('')


PPDB = []
PP = {}
for L in I:
    if L:
        L = L.split()
        for ab in L:
            a,b = ab.split(':')
            PP[a] = b
    else:
        PPDB.append(PP)
        PP = {}


# Part 1
ReqFields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
PPDB = [PP for PP in PPDB if all(field in PP for field in ReqFields)]
print(len(PPDB))


# Part 2
ValidECL = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
def valid(PP):
    try:
        return \
            1920<=int(PP['byr'])<=2002                               and \
            2010<=int(PP['iyr'])<=2020                               and \
            2020<=int(PP['eyr'])<=2030                               and \
            ((PP['hgt'][-2:]=='cm' and 150<=int(PP['hgt'][:-2])<=193) or \
             (PP['hgt'][-2:]=='in' and 59<=int(PP['hgt'][:-2])<=76)) and \
            PP['ecl'] in ValidECL                                    and \
            re.match(r'#[0-9a-f]{6}$', PP['hcl'])                    and \
            re.match(r'[0-9]{9}$', PP['pid'])
    except ValueError:
        return False

PPDB = [PP for PP in PPDB if valid(PP)]
print(len(PPDB))
