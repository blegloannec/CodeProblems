#!/usr/bin/env python

import sys

memo = {}
cont = []

# nb de solutions pour un volume l avec les n+1 premiers containers
def progdyn(n,l):
    if l==0:
        return 1
    if n<0:
        return 0
    if (n,l) in memo:
        return memo[(n,l)]
    res = progdyn(n-1,l)
    if l>=cont[n]:
        res += progdyn(n-1,l-cont[n])
    memo[(n,l)] = res
    return res

memo2 = {}

# nb de solutions pour un volume l avec les n+1 premiers containers
# et en utilisant au plus nbc containers
def progdyn2(n,l,nbc):
    if l==0:
        return 1
    if n<0 or nbc<=0:
        return 0
    if (n,l,nbc) in memo2:
        return memo2[(n,l,nbc)]
    res = progdyn2(n-1,l,nbc)
    if l>=cont[n]:
        res += progdyn2(n-1,l-cont[n],nbc-1)
    memo2[(n,l,nbc)] = res
    return res

def main():
    global cont
    f = open(sys.argv[1],'r')
    cont = map(int,f.readlines())
    f.close()
    print progdyn(len(cont)-1,150)
    for i in range(1,len(cont)+1):
        print i,progdyn2(len(cont)-1,150,i)

main()
