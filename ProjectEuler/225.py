#!/usr/bin/env python

def tribo(p):
    a,b,c = 1,1,1
    vu = set()
    while (a,b,c) not in vu:
        vu.add((a,b,c))
        a,b,c = b,c,(a+b+c)%p
        if c==0:
            return False
    return True
    
def main():
    cpt = 0
    i = 3
    while cpt<124:
        if tribo(i):
            cpt += 1
        i += 2
    print i-2

main()
