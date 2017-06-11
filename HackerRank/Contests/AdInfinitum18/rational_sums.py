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

# pour calculer P(x)
def horner(B,x):
    res = 0
    for i in range(len(B)-1,-1,-1):
        res = (x*res + B[i])%P
    return res

# Q'(x) pour x dans A
def Qp(A,x):
    res = 1
    for q in A:
        if x!=q:
            res = (res*(x-q))%P
    return res

# petites sommes partielles de la serie harmonique
H0 = [0]
for i in range(1,5001):
    H0.append((H0[i-1]+inv_mod(i))%P)

def H(n):
    if n>=0:
        return H0[n]
    return -H0[-n]

def main():
    n = int(input())
    A = list(map(int,input().split()))
    A = [-a for a in A]
    B = list(map(int,input().split()))
    res = 0
    # pour x dans A, le coeff. de 1/(X-x) dans la decomposition en elements
    # simples est P(x)/Q'(x), la "limite" de la serie de ce terme est
    # coeff(x) * (H(x) + lim_n H(n)) qui, pris individuellement, diverge mais
    # la somme des coeff(x) vaut 0 et donc la somme des coeff(x) * lim_n H(n)
    # s'annule (sinon cela divergerait) et finalement la limite de la serie
    # est simplement la somme des coeff(x) * H(x)
    for i in range(n):
        res = (res + (H(A[i])*(horner(B,A[i])*inv_mod(Qp(A,A[i])))%P)%P)%P
    print(res)

main()
