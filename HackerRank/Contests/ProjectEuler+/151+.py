#!/usr/bin/env python3

M = 10**9+7

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a//b)*v)

def inv_mod(a,n=M):
    _,u,_ = bezout(a,n)
    return u

memo = {}
def E(conf):
    if conf in memo:
        return memo[conf]
    res,size = 0,0
    for pick in range(len(conf)):
        if conf[pick]>0:
            size += conf[pick]
            new = list(conf)
            new[pick] -= 1
            for a in range(pick+1,len(conf)):
                new[a] += 1
            res = (res + conf[pick]*E(tuple(new)))%M
    res = (res*inv_mod(size))%M
    if size==1:
        res = (res+1)%M
    memo[conf] = res
    return res

def main():
    N = int(input())
    memo[tuple(0 for _ in range(N))] = 0
    E(tuple(int(i==0) for i in range(N)))
    for conf in sorted(memo):
        print('%s: %d' % (' '.join(map(str,conf)),memo[conf]))

main()
