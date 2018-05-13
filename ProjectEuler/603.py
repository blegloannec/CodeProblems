#!/usr/bin/env pypy

# on fixe n et k et l'on pose L = taille de S
# la contribution du chiffre S_i, pour 0<=i<L, au total C(N,K) est
# S_i * sum_{k=0..K-1} [ (i+kL+1) * sum_{j=0..(K-k)L-i-1} 10^j ]
#        ( depart de l'intervalle * fin et 10^decalage associe )
# S_i * sum_{k=0..K-1} [ (i+1 + kL) * (10^(K-k)L-i) - 1) / 9 ]
# puis on developpe en 4 sommes dont on calcule les formules explicites
# (cf. le code ci-dessous pour la formule)

# runs in <10s with pypy (but could be more optimized)

P = 10**9+7

def inv(n):
    return pow(n,P-2,P)

def sieve_list(N):
    P = [True]*N
    L = []
    for i in xrange(2,N):
        if P[i]:
            L.append(i)
            for k in xrange(2*i,N,i):
                P[k] = False
    return L

def C(N,K):
    S = ''.join(map(str,sieve_list(16*N)[:N]))
    L = len(S)
    KP = K%P
    R = pow(inv(10),L,P)
    Const1 = ((pow(R,K,P)-1)*inv(R-1)*pow(10,K*L,P))%P
    Const2 = (L*(((KP-1)*R-K)*pow(R,K,P)+R)*inv((1-R)**2)*pow(10,K*L,P))%P
    Const3 = (L*KP*(KP-1)*inv(2))%P
    I10 = inv(10)
    res = 0
    for i in xrange(L):
        C = int(S[i])
        #res = (res + C*(i+1)*pow(10,K*L-i,P)*(pow(R,K,P)-1)*inv(R-1)) % P
        res = (res + C*(i+1)*pow(I10,i,P)*Const1) % P
        res = (res - C*(i+1)*KP) % P
        #res = (res + C*L*pow(10,K*L-i,P)*(((KP-1)*R-K)*pow(R,K,P)+R)*inv((1-R)**2)) % P
        res = (res + C*pow(I10,i,P)*Const2) % P
        #res = (res - C*L*KP*(KP-1)*inv(2)) % P
        res = (res - C*Const3) % P
    res = (res*inv(9))%P
    return res

print C(10**6,10**12)
