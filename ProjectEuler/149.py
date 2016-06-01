#!/usr/bin/env python

S = []
def gen():
    for k in xrange(1,56):
        S.append(((100003-200003*k+300007*k*k*k)%1000000)-500000)
    for k in xrange(56,4000001):
        S.append(((S[-24]+S[-55]+1000000)%1000000)-500000)

# Carre n*n
# les elements d'une meme ligne k sont les indices :
# k*n+i, i=0..n-1
# les elements d'une meme colonne k sont les indices :
# k+n*i, i=0..n-1
# les elements d'une meme diagonale k sont les indices :
# k+(n+1)*i, i=0..n-1-k (pt de depart sur la premiere ligne)
# n*k+(n+1)*i, i=0..n-1-k (pt de depart sur la premiere colonne)
# les elements d'une meme anti-diagonale k sont les indices :
# k+(n-1)*i, i=0..k (pt de depart sur la premiere ligne)
# n*(n-1)+k-(n-1)*i, i=0..k (pt de depart sur la derniere ligne)
        
# progdyn lineaire max somme consecutive
def maxsum(T):
    M = 0
    M0 = 0
    for t in T:
        M0 = t+max(M0,0)
        if M0>M:
            M = M0
    return M
        
def main():
    gen()
    N = 2000
    M = 0
    for k in xrange(N):
        M = max(M,maxsum([S[k*N+i] for i in xrange(N)]))
        M = max(M,maxsum([S[k+N*i] for i in xrange(N)]))
        M = max(M,maxsum([S[k+(N+1)*i] for i in xrange(N-k)]))
        M = max(M,maxsum([S[k+(N-1)*i] for i in xrange(k+1)]))
        if k>=1:
            M = max(M,maxsum([S[N*k+(N+1)*i] for i in xrange(N-k)]))
            M = max(M,maxsum([S[N*(N-1)+k-(N-1)*i] for i in xrange(k+1)]))
    print M

main()
