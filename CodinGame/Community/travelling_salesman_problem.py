#!/usr/bin/env python3

from math import sqrt

# TSP greedy approx in O(n^2)

def dist2(A,B):
    return (A[0]-B[0])**2 + (A[1]-B[1])**2

def tsp_greedy(P):
    for i in range(len(P)-2):
        j = min(range(i+1,len(P)), key=(lambda j: dist2(P[i],P[j])))
        P[i+1],P[j] = P[j],P[i+1]

def main():
    N = int(input())
    P = [tuple(map(int,input().split())) for _ in range(N)]
    tsp_greedy(P)
    d = sum(sqrt(dist2(P[i],P[(i+1)%N])) for i in range(len(P)))
    print(round(d))

main()
