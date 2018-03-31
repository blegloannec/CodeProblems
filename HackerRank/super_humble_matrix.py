#!/usr/bin/env python3

# les elements presents sur chaque diagonale sont imposes
# mais on peut permuter l'ordre de ces elements librement

P = 10**9+7

M,N = map(int,input().split())
if M<N:
    M,N = N,M

# fact mod
F = [1]*(N+1)
for n in range(2,N+1):
    F[n] = (n*F[n-1]) % P

res = 1
for n in range(1,N):
    res = (res * pow(F[n],2,P)) % P
res = (res * pow(F[N],M-N+1,P)) % P
print(res)
