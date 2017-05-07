#!/usr/bin/env python3

n = int(input())
B = []
for _ in range(n):
    h,x1,x2 = map(int,input().split())
    B.append((h,x1,x2))

# algo naif en O(n*max_width)
W = 5000
H = [0]*(W+2)
def naive():
    for (h,x1,x2) in B:
        for i in range(x1+1,x2+1):
            if h>H[i]:
                H[i] = h
    cpt = -1
    for i in range(W+1):
        if H[i]!=H[i+1]:
            cpt += 2
    return cpt

#print(naive())

# diviser pour regner en O(n log n)
def skyline_merge_sort(i=0,j=len(B)-1):
    if i==j:
        h,x1,x2 = B[i]
        return [(x1,h),(x2,0)]
    k = (i+j)//2
    B1 = skyline_merge_sort(i,k)
    B2 = skyline_merge_sort(k+1,j)
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

print(2*len(skyline_merge_sort())-1)
