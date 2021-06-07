#!/usr/bin/env python3

import re

cols = lambda C: not any(re.search(r'[^ ]:', L) for L in C)
ifs  = lambda C: not any(re.search(r'if *[^ (]', L) for L in C)

def indt(Code):
    s0 = 0
    for L in Code:
        s = re.match(r' *', L).span()[1]
        if abs(s-s0)>1:
            return False
        s0 = s
    return True

empt = lambda C: any(all(L=='' for L in C[l::2]) for l in (0,1))
_com = lambda L: re.match(r'#|//', L) is not None
docs = lambda C: any(all(_com(L) for L in C[l::2]) for l in (0,1))
doc5 = lambda C: all(_com(L) for L in C[:5])

def main():
    N = int(input())
    C = int(input())
    Friends = []
    for _ in range(N):
        name,*tics = input().split()
        Friends.append((name, set(tics)))
    Code = [input() for _ in range(C)]
    Tics = set(t for t,f in ((':',cols), ('if',ifs), ('t',indt),  \
                             ('n',empt), ('#',docs), ('5#',doc5)) \
               if f(Code))
    print(next(name for name,tics in Friends if tics<=Tics))

main()
