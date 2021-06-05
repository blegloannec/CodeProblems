#!/usr/bin/env python3

# good enough O(3^|N|) brute-force
from itertools import product
def brute():
    for P in product(['','+','-'], repeat=len(N)-1):
        E = ''.join(a+b for a,b in zip(N,P)) + N[-1]
        if eval(E)==K:
            print(E)


# Backtracking with memoization
Sol = []
cut = set()
def dp(k,i=0):
    if i==len(N):
        if k==0:
            print(''.join(Sol))
        return k==0
    if (k,i) not in cut:
        worth = False
        for j in range(len(N),i,-1):
            Sol.append(('+' if i>0 else '') + N[i:j])
            worth |= dp(k-int(N[i:j]),j)
            Sol.pop()
        if i>0:
            for j in range(len(N),i,-1):
                Sol.append('-' + N[i:j])
                worth |= dp(k+int(N[i:j]),j)
                Sol.pop()
        if not worth:
            cut.add((k,i))
        return worth
    return False    


if __name__=='__main__':
    N = input()
    K = int(input())
    #brute()
    dp(K)
