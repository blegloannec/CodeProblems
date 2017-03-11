#!/usr/bin/env python3

# on remarque que
# a(6i) = 3i
# a(6i+1) = 4i+1
# a(6i+2) = 3i+1
# a(6i+3) = i
# a(6i+4) = 3(2i+1)
# a(6i+5) = i

# soit S(n) = sum(a_i, i=1..n)
# la sequence des S(k) modulo M sera periodique de periode 6*M

# soit A(p,q) = sum(a(i), i=p..q) mod M = (S(p) - S(q)) mod M
# donc A(p,q) = 0 mod M <=> S(p) = S(q) mod M

# and BTW see also http://oeis.org/A001710 (not relevant for that pb though)

def f(N,M):
    N += 1
    P = 6*M
    # calcul des sommes partielles de la periode
    S = [0]
    for n in range(1,P):
        i = n//6
        if n%6==0:
            a = 3*i
        elif n%6==1:
            a = 4*i+1
        elif n%6==2:
            a = 3*i+1
        elif n%6==3 or n%6==5:
            a = i
        else:
            a = 3*(2*i+1)
        S.append((S[-1]+a)%M)
    # on compte les valeurs apparaissant jusqu'a N
    Cpt = [0]*M
    for i in range(P): # compte sur la periode
        Cpt[S[i]] += 1
    R = N//P
    for i in range(M): # repetition
        Cpt[i] *= R
    for i in range(N%P): # complement
        Cpt[S[i]] += 1
    # on deduit le nb de couples
    res = 0
    for i in range(M):
        res += Cpt[i]*(Cpt[i]-1)//2
    return res

#print(f(10,10))
#print(f(10**4,10**3))
print(f(10**12,10**6))
