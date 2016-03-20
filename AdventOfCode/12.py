#!/usr/bin/env python

import sys
import re,json,types

re1 = re.compile('-?[0-9]+')

def cpt(doc):
    if type(doc)==types.ListType:
        return sum(map(cpt,doc))
    elif type(doc)==types.DictType:
        c = 0
        for k in doc:
            if doc[k]=='red':
                return 0
            c += cpt(doc[k])
        return c
    elif type(doc)==types.IntType:
        return doc
    return 0

def main():
    f = open(sys.argv[1],'r')
    doc = f.read()
    f.close()
    print sum(map(int,re1.findall(doc)))
    ddoc = json.loads(doc)
    print cpt(ddoc)

main()
