#!/usr/bin/env python3

guard = lambda s: f'^{s}$'

def match(P, S):
    i = 0
    for p in P:
        j = S.find(p, i)
        if j<0:
            return False
        i = j + len(p)
    return True        

def main():
    P = guard(input()).split('*')
    P = [w for w in P if w!='']
    N = int(input())
    for _ in range(N):
        L = input()
        if match(P, guard(L)):
            print(L)

main()
