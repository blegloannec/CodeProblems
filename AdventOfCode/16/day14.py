#!/usr/bin/env python

import hashlib, re

Input = 'yjdafjpo'

def md5(s):
    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()

def stretch(s):
    for i in xrange(2017):
        s = md5(s)
    return s

P = []
def get_hash(i):
    if i==len(P):
        # use that line for Part One:
        P.append(md5(Input+str(i)))
        # or that line for Part Two: (~40s with pypy)
        #P.append(stretch(Input+str(i)))
    return P[i]

triple = re.compile('(.)\\1\\1')

def gen_keys():
    cpt = 0
    i = 0
    while cpt<64:
        O = triple.search(get_hash(i))
        if O!=None:
            s = O.group(1)*5
            for j in xrange(i+1,i+1001):
                if get_hash(j).find(s)>=0:
                    cpt += 1
                    break
        i += 1
    return i-1

print gen_keys()
