#!/usr/bin/env python3

import sys
input = sys.stdin.readline

# Idea: If we can form a string "abcde" of odd size 2n-1
#       then we have a n x n solution: abc
#                                      bcd
#                                      cde
# The converse is true by taking the first line + last column
# of any valid solution.

N = 26
num = lambda c: ord(c)-ord('a')

def _dfs_cycle(Seen, Visited, Pred, u):
    for v in range(N):
        if M[u][v] and not Visited[v]:
            if not Seen[v]:
                Pred[v] = u
                Seen[v] = True
                C = _dfs_cycle(Seen, Visited, Pred, v)
                if C is not None:
                    return C
            else:  # cycle found
                C = []
                while u!=v:
                    C.append(u)
                    u = Pred[u]
                C.append(v)
                C.reverse()
                return C
    Visited[u] = True
    return None

def dfs_cycle():
    Seen = [False]*N
    Visited = [False]*N
    Pred = [None]*N
    for u in range(N):
        if not Seen[u]:
            Seen[u] = True
            C = _dfs_cycle(Seen, Visited, Pred, u)
            if C is not None:
                return C
    return None

def dag_longest_path(Length, Succ, u):
    if Length[u] is None:
        Length[u] = 0
        for v in range(N):
            if M[u][v]:
                l = dag_longest_path(Length, Succ, v)
                if l+1>Length[u]:
                    Length[u] = l+1
                    Succ[u] = v
    return Length[u]

def main():
    global M
    T = int(input())
    for _ in range(T):
        F = int(input())
        # matrix of the digraphs graph
        M = [[True]*N for _ in range(N)]
        for _ in range(F):
            dg = input()
            M[num(dg[0])][num(dg[1])] = False
        # we look for a cycle
        C = dfs_cycle()
        if C is not None:
            # then we only need 2*20-1 chars
            while len(C)<39:
                C += C
            C = C[:39]
        else:
            # otherwise we use DP on the DAG to find
            # a longest path and build a solution from it
            Length = [None]*N
            Succ = [None]*N
            u0 = 0
            for u in range(N):
                l = dag_longest_path(Length, Succ, u)
                if l>Length[u0]:
                    u0 = u
            C = []
            while u0 is not None:
                C.append(u0)
                u0 = Succ[u0]
        C = ''.join(chr(i+ord('a')) for i in C)
        s = (len(C)+1)//2
        sys.stdout.write('\n'.join(C[i:i+s] for i in range(s)))
        sys.stdout.write('\n')

main()
