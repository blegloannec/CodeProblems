#!/usr/bin/env python3

# la contribution totale du segment d'indices l a r est
# s(l,r) = 2^max(0,l-1) * (r-l+1)*(T[l]+...+T[r]) * 2^max(0,n-1-r-1)
# (avec les max(0,.) pour les cas particuliers l=0 ou r=n-1)
# la contribution de tous les blocs commencant a l'indice l
# S(l) = sum( s(l,r), l<=r<n )
#      = 2^max(0,l-1) * sum( (r-l+1)*(T[l]+...+T[r]) * 2^max(0,n-1-r-1), l<=r<n)
#      = 2^max(0,l-1) * sum( sum((r-l+1)*T[i]*2^max(0,n-1-r-1), l<=i<=r), l<=r<n)
#      = 2^max(0,l-1) * sum( sum((r-l+1)*T[i]*2^max(0,n-1-r-1), l<=i<=r), l<=r<n)
#      = 2^max(0,l-1) * sum((r-l+1)*T[i]*2^max(0,n-1-r-1), l<=i<=r<n)
#      = 2^max(0,l-1) * sum(T[i]*sum((r-l+1)*2^max(0,n-1-r-1), i<=r<n), l<=i<n)
#      = 2^max(0,l-1) * sum(T[i]*(sum((r-l+1)*2^(n-1-r-1), i<=r<=n-2) + n-l), l<=i<n)
#      = 2^max(0,l-1) * sum(T[i]*((i-l+2)*2^(n-1-i) + l-n-1 + n-l), l<=i<n)
#      = 2^max(0,l-1) * sum(T[i]*((i-l+2)*2^(n-1-i) - 1), l<=i<n)
# le total
# S = sum( S(l), 0<=l<n )
#   = sum( 2^max(0,l-1) * sum( T[i]*((i-l+2)*2^(n-1-i) - 1), l<=i<n), 0<=l<n )
#   = sum( T[i] * ((i+2)*2^(n-1-i)-1 + sum( 2^(l-1)*((i-l+2)*2^(n-1-i)-1), 0<l<=i ), 0<=i<n )
#   = sum( T[i] * ((i+2)*2^(n-1-i)-1 + 2^(n-1-i)*sum(2^(l-1)*(i-l+2), 0<l<=i) - sum(2^(l-1), 0<l<=i), 0<=i<n )
#   = sum( T[i] * ((i+2)*2^(n-1-i)-1 + 2^(n-1-i)*(-3+3*2^i-i) - (2^i-1)), 0<=i<n )
#   = sum( T[i] * (3*2^(n-1) - 2^(n-1-i) - 2^i), 0<=i<n )
# la contribution finale de T[i] est tres simple et presente une belle symetrie,
# pouvait-on la deduire plus directement et moins techniquement ?...

P = 10**9+7

n = int(input())
T = list(map(int,input().split()))

S = 0
for i in range(n):
    S = (S + T[i] * (3*pow(2,n-1,P) - pow(2,n-1-i,P) - pow(2,i,P)) ) % P
print(S)
