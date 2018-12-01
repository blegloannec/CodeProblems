#!/usr/bin/env python3

import sys

I = list(map(int,sys.stdin.readlines()))

# Part 1
print(sum(I))


# Part 2
## Method 1 (expected): naive simulation
from itertools import cycle

def naive(I):
    S = 0
    seen = {S}
    for x in cycle(I):
        S += x
        if S in seen:
            break
        seen.add(S)
    return S

print(naive(I))

## Method 2: O(n log n) approach
from collections import defaultdict

def efficient(I):
    N = len(I)
    S = sum(I)
    neg = S<0
    S = abs(S)
    # when S < 0, we take the opposite of S and I
    # so that in the following, we have S >= 0
    Pref = [-i if neg else i for i in I]
    for i in range(1,N):
        Pref[i] += Pref[i-1]
    # Each time we pass on I[i], the sum is Pref[i] + k*S for k = 0,1,...
    # Hence if Pref[i] + k*S = Pref[j] + l*S (repeated sum) then:
    #  1. Pref[i] = Pref[j] mod S
    #  2. assuming S>=0 and e.g. Pref[i]<=Pref[j], we have
    #     Pref[i] + (k-l)*S = Pref[j] with k-l>=0
    #     so that passing on i after k-l cycles gives the same
    #     value as j on the *first* cycle, thus the first repeated
    #     value is a value that appeared for the first time within
    #     the first pass on I
    
    # We group the indices i by their value of Pref[i] mod S
    Group = defaultdict(list)
    for i in range(N):
        Group[Pref[i]%S].append(i)
    
    tmin,f = float('inf'),None
    for r in Group:
        if len(Group[r])>1:
            # We sort the indices of the group in increasing order of Pref[.]
            # and in decreasing order of index in case of equality
            Group[r].sort(key=(lambda i: (Pref[i],-i)))
            # then we only examine the time it takes for the i-th index
            # sum sequence to catch the (i+1)-th index original value
            # the "optimal" is necessarily among these "consecutive catch"
            for i in range(len(Group[r])-1):
                a,b = Group[r][i],Group[r][i+1]
                t = a + N*(Pref[b]-Pref[a])//S
                if t<tmin:
                    tmin,f = t,Pref[b]
    return -f if neg else f

#print(efficient(I))
