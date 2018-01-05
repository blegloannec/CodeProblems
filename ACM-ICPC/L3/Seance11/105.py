#!/usr/bin/env python3

import sys

# diviser pour regner en O(n log n)
def skyline_merge_sort(N,i,j):
    if i==j:
        h,x1,x2 = B[i]
        return [(x1,h),(x2,0)]
    k = (i+j)//2
    B1 = skyline_merge_sort(B,i,k)
    B2 = skyline_merge_sort(N,k+1,j)
    i1,i2 = 0,0  # incides courants
    h1,h2 = 0,0  # hauteurs courantes
    A = []
    while i1<len(B1) or i2<len(B2):
        if i1==len(B1) or (i2<len(B2) and B2[i2][0]<B1[i1][0]):
            x,h2 = B2[i2]
            i2 += 1
        elif i2==len(B2) or B1[i1][0]<B2[i2][0]:
            x,h1 = B1[i1]
            i1 += 1
        else:
            x,h1 = B1[i1]
            _,h2 = B2[i2]
            i1 += 1
            i2 += 1
        h = max(h1,h2)
        if len(A)==0 or A[-1][1]!=h: # nouveau point
            A.append((x,h))
    return A

def main():
    global B
    B = []
    for L in sys.stdin.readlines():
        x1,h,x2 = map(int,L.split())
        B.append((h,x1,x2))
    A = skyline_merge_sort(B,0,len(B)-1)
    S = ' '.join('%d %d'%x for x in A)
    print(S)

main()
