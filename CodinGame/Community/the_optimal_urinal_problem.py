#!/usr/bin/env python3

# see also PE 472

def urinals(n):
    if n<=2:
        return 1,1
    # DP in O(n)
    # DP[n] = max nb of people we can place in
    #         the 10^n1 configuration
    DP = [0]*n
    for i in range(3,n):
        m = i//2
        DP[i] = 1 + DP[m] + DP[i-1-m]
    # computing result in O(n)
    imax = 0
    kmax = DP[n-2]+2
    if n>=4:
        for i in range(1,(n+1)//2):
            # the first 3 people go to positions
            # i, 0 (if i>1) and n-1
            k = 1 + DP[i-1]+int(i>1) + DP[n-2-i]+1
            if k>kmax:
                kmax = k
                imax = i
    return kmax,imax+1

def main():
    n = int(input())
    print(*urinals(n))

main()
