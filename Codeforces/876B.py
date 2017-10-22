#/usr/bin/env python3

n,k,m = map(int,input().split())
A = list(map(int,input().split()))
R = [[] for _ in range(m)]
rmax = 0
for a in A:
    r = a%m
    R[r].append(a)
    if len(R[r])>len(R[rmax]):
        rmax = r
if len(R[rmax])>=k:
    print('Yes')
    print(' '.join(map(str,R[rmax][:k])))
else:
    print('No')
