#!/usr/bin/env python3

# Generic approach through automaton
# State 0: no 6 or 8 read yet
#       1: 6 read, final
#       2: 8 read, final

#     0  1  2  3  4  5  6  7  8  9 
A = [[0, 0, 0, 0, 0, 0, 1, 0, 2, 0],
     [1, 1, 1, 1, 1, 1, 1, 1,-1, 1],
     [2, 2, 2, 2, 2, 2,-1, 2, 2, 2]]

memo = {(0,0):0, (0,1):1, (0,2):1}
def count_words(l,s=0):
    if (l,s) in memo:
        return memo[l,s]
    res = 0
    for a in range(10):
        if A[s][a]>=0:
            res += count_words(l-1,A[s][a])
    memo[l,s] = res
    return res

def count_under(N,l,s=0):
    if l==0:
        return count_words(l,s)
    res = 0
    n = int(N[-l])
    for a in range(n):
        if A[s][a]>=0:
            res += count_words(l-1,A[s][a])
    if A[s][n]>=0:
        res += count_under(N,l-1,A[s][n])
    return res

def main():
    L,R = input().split()
    L = str(int(L)-1)
    print(count_under(R,len(R))-count_under(L,len(L)))

main()
