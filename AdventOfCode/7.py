#!/usr/bin/env python

import sys
import re
import types

t = [[False for j in range(1000)] for i in range(1000)]

instr = re.compile('(.+) -> ([a-z]+)')
const = re.compile('[0-9]+$')
signal = re.compile('[a-z]+$')
op1 = re.compile('NOT ([a-z0-9]+)$')
op2 = re.compile('([a-z0-9]+) ([A-Z]+) ([a-z0-9]+)$')

D = {}

def evaluate(sig):
    if const.match(sig)!=None:
        return int(sig)
    f = D[sig]
    if type(f)==types.IntType:
        return f
    p = const.match(f)
    if p!=None:
        res = int(f)
        D[sig] = res
        return res
    p = signal.match(f)
    if p!=None:
        res = evaluate(f)
        D[sig] = res
        return res
    p = op1.match(f)
    if p!=None:
        res = ~evaluate(p.group(1))
        D[sig] = res
        return res
    p = op2.match(f)
    a1 = evaluate(p.group(1))
    a2 = evaluate(p.group(3))
    if p.group(2)=='AND':
        res = a1 & a2
    elif p.group(2)=='OR':
        res = a1 | a2
    elif p.group(2)=='RSHIFT':
        res = a1 >> a2
    else:
        res = (a1 << a2)%65536
    D[sig] = res
    return res

def main():
    global D
    f = open(sys.argv[1],'r')
    cases = f.readlines()
    f.close()
    for l in cases:
        s = l.strip()
        p = instr.match(s)
        D[p.group(2)] = p.group(1)
    D['b'] = 16076
    print evaluate('a')

main()
