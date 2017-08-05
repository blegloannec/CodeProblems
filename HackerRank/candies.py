#!/usr/bin/env python3

# O(N log N) simple approach, distributing candies to increasing ratings

# this can also be solved in O(N) through several (slightly more technical)
# ways, see editorial for instance

def main():
    N = int(input())
    R = [(int(input()),i) for i in range(N)]
    C = [0]*N
    for v,i in sorted(R):
        a = C[i-1] if i>0 and R[i-1][0]<v else 0
        b = C[i+1] if i<len(C)-1 and R[i+1][0]<v else 0
        C[i] = max(a,b)+1
    print(sum(C))

main()
