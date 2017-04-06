#!/usr/bin/env python3

# so uninspired Problem of the Week!...

def simu(Trans,T,q,x):
    Tape = [0]*T
    t = 0
    while 0<=x<T and q!='HALT':
        Tape[x],dx,q = Trans[q,Tape[x]]
        x += dx
        t += 1
    return t,x,Tape
    

def main():
    S,T,X = map(int,input().split())
    START = input()
    N = int(input())
    Trans = {}
    Dir = {'L':-1,'R':1}
    for _ in range(N):
        s,t = input().split(':')
        t = t.split(';')
        for a in range(S):
            w,m,n = t[a].split()
            Trans[s,a] = (int(w),Dir[m],n)
    t,x,Tape = simu(Trans,T,START,X)
    print(t)
    print(x)
    print(''.join(map(str,Tape)))

main()
