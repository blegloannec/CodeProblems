#!/usr/bin/env python

W = [(8,4,0),(10,5,0),(25,6,0),(40,7,0),(74,8,0)]
A = [(0,0,0),(13,0,1),(31,0,2),(53,0,3),(75,0,4),(102,0,5)]
R = [(25,1,0),(50,2,0),(100,3,0),(20,0,1),(40,0,2),(80,0,3)]

def stats(w,a,rs):
    s = []
    for i in range(3):
        x = W[w][i]+A[a][i]
        for r in rs:
            x += R[r][i]
        s.append(x)
    return tuple(s)

def winner(ph,pd,pa):
    bh,bd,ba = 100,8,2
    prd = max(1,pd-ba)
    brd = max(1,bd-pa)
    pturns = bh/prd+(1 if bh%prd>0 else 0)
    bturns = ph/brd+(1 if ph%brd>0 else 0)
    return (pturns<=bturns)

minm = 1000
def test1((pm,pd,pa)):
    global minm
    if pm<minm and winner(100,pd,pa):
        minm = pm
        
maxm = -1
def test2((pm,pd,pa)):
    global maxm
    if pm>maxm and not winner(100,pd,pa):
        maxm = pm

def test(s):
    test1(s)
    test2(s)
        
def main():
    for w in range(len(W)):
        for a in range(len(A)):
            test(stats(w,a,[]))
            for r1 in range(len(R)):
                test(stats(w,a,[r1]))
                for r2 in range(r1+1,len(R)):
                    test(stats(w,a,[r1,r2]))
    print minm,maxm

main()
