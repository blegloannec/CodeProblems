#!/usr/bin/env python3

def prev_tidy(n):
    n = list(map(int,str(n)))
    curr,i0,i = n[0],0,1
    while i<len(n) and curr<=n[i]:
        if curr<n[i]: # new block
            curr = n[i]
            i0 = i
        i += 1
    if i<len(n): # n not tidy
        # -1 on the first digit of the current block
        n[i0] -= 1
        # and the rest goes to 9
        for j in range(i0+1,len(n)):
            n[j] = 9
    res = 0
    for x in n:
        res = 10*res + x
    return res

def main():
    T = int(input())
    for t in range(1,T+1):
        N = int(input())
        print('Case #%d: %d' % (t,prev_tidy(N)))

main()
