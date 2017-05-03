#!/usr/bin/env python3

P = 10**9+7

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a//b)*v)

def inv_mod(a,n=P):
    _,u,_ = bezout(a,n)
    return u

N = 5*10**5+1
F = [1]
Finv = [1]
for n in range(1,N):
    F.append((F[-1]*n)%P)
    Finv.append(inv_mod(F[-1]))

def binom(n,p):
    return (F[n]*(Finv[p]*Finv[n-p])%P)%P

def main():
    q = int(input())
    for _ in range(q):
        s = input()
        C = [0]*4
        for c in s:
            C[ord(c)-ord('a')] += 1
        Xab = 0
        for i in range(min(C[0],C[1])+1):
            Xab = (Xab + binom(C[0],i)*binom(C[1],i))%P
        Xcd = 0
        for i in range(min(C[2],C[3])+1):
            Xcd = (Xcd + binom(C[2],i)*binom(C[3],i))%P
        print((Xab*Xcd-1)%P)

main()
