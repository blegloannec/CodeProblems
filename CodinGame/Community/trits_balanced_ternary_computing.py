#!/usr/bin/env python3

from operator import add,sub,mul
Ops = {'+':add, '-':sub, '*':mul}

D = 'T01'
Dinv = {D[i]:i-1 for i in range(3)}

def tern2dec(t):
    res = 0
    for d in t:
        res = 3*res + Dinv[d]
    return res

def dec2tern(n):
    T = []
    while n:
        n,r = divmod(n+1,3)
        T.append(D[r])
    res = ''.join(reversed(T))
    return res if res else '0'

if __name__=='__main__':
    L = input()
    op = input()
    r = tern2dec(input())
    if op=='<<':
        res = L + '0'*r
    elif op=='>>':
        res = L[:-r] if r<len(L) else '0'
    else:
        l = tern2dec(L)
        res = dec2tern(Ops[op](l,r))
    print(res)
