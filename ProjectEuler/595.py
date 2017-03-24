#!/usr/bin/env python3

# si on considere un decoupage quelconque
# ...|..|.|...
# on peut *toujours* remplir par blocs :
# 789|56|4|123   (une methode par exemple)
# donc tout decoupage est possible

# considerons une permutation de S_(n-1) en k blocs
# pour fabriquer une permutation de S_n, on a
# n positions pour inserer le n
# 1. si on l'insere apres le n-1, on a encore k blocs
#    cela correspond a une seule position d'insertion
# 2. si on l'insere entre 2 blocs, mais pas apres n-1,
#    on forme k+1 blocs
#    cela correspond a exactement k positions d'insertion
# 3. si on l'insere au "milieu" d'un bloc, on forme k+2 blocs
#    par elimination, cela correspond a n-k-1 positions
#    d'insertion

N = 52

# factorielles
F = [1]
for n in range(1,N+1):
    F.append(F[-1]*n)

# B(n,k) le nombre de permutations de n elements
# en exactement 1<=k<=n blocs
memo = {}
def B(n,k):
    if n==1 or k==1:
        return int(k==1)
    if (n,k) in memo:
        return memo[n,k]
    res = (k-1)*B(n-1,k-1)     # cas 2 du raisonnement
    if k<=n-1:                 # cas 1
        res += B(n-1,k)
    if n-(k-2)-1>0 and k-2>0:  # cas 3
        res += (n-(k-2)-1)*B(n-1,k-2)
    memo[n,k] = res
    return res

# on a alors clairement
# S(n) = sum( (1+S(k)) * B(n,k) / n!, k=2..n )
# n! * S(n) = sum( (1+S(k)) * B(n,k), k=2..n-1 ) + B(n,n)*(1+S(n))
# (n!-B(n,n)) * S(n) = sum( (1+S(k)) * B(n,k), k=2..n-1 ) + B(n,n)

T = [-1]*(N+1)
T[1] = 0
def S(n):
    if T[n]>=0:
        return T[n]
    T[n] = (sum((1+S(k))*B(n,k) for k in range(2,n))+B(n,n)) / (F[n]-B(n,n))
    return T[n]

print(S(N))
