#!/usr/bin/env python3

# glouton facile, on choisit chaque jour un cours
# restant par l'entraineur ayant le plus grand niveau
# de sadness (implementation en utilisant un tas)

from heapq import *

def main():
    T = int(input())
    for _ in range(T):
        N,D = map(int,input().split())
        A = [[] for _ in range(D)]
        for _ in range(N):
            Di,Ti,Si = map(int,input().split())
            Di -= 1
            A[Di].append((Ti,Si))
        H = []
        for d in range(D):
            for (Ti,Si) in A[d]:
                heappush(H,(-Si,Ti))
            if H:
                mSi,Ti = heappop(H)
                if Ti>1:
                    heappush(H,(mSi,Ti-1))
        res = 0
        for (mSi,Ti) in H:
            res += -mSi*Ti
        print(res)

main()
