#!/usr/bin/env python

import sys
import hashlib

def salt(data,nz):
    pref = nz*'0'
    s = 0
    while True:
        m = hashlib.md5(data)
        m.update(str(s))
        h = m.hexdigest()
        if h[:nz]==pref:
            return s
        s += 1

def main():
    f = open(sys.argv[1],'r')
    cases = f.readlines()
    f.close()
    for l in cases:
        print salt(l.strip(),5),salt(l.strip(),6)

main()
