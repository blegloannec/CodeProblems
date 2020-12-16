#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def main():
    N = int(input())
    P = []
    for _ in range(N):
        name,s1,s2,s3 = input().split()
        P.append((name, int(s1), int(s2), int(s3)))
    S1 = sorted(range(N), key=(lambda i: (-P[i][1], P[i][0])))
    S2 = sorted(range(N), key=(lambda i: (-P[i][2], P[i][0])))
    S3 = sorted(range(N), key=(lambda i: (-P[i][3], P[i][0])))
    Avail = [True]*N
    i = j = k = 0
    while True:
        while i<N and not Avail[S1[i]]: i += 1
        if i==N: break
        Avail[S1[i]] = False
        while j<N and not Avail[S2[j]]: j += 1
        if j==N: break
        Avail[S2[j]] = False
        while k<N and not Avail[S3[k]]: k += 1
        if k==N: break
        Avail[S3[k]] = False
        Team = [P[S1[i]][0], P[S2[j]][0], P[S3[k]][0]]
        Team.sort()
        sys.stdout.write(' '.join(Team))
        sys.stdout.write('\n')
        i += 1
        j += 1
        k += 1

main()
