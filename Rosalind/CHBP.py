#!/usr/bin/env python3

# n feuilles, n-2 noeuds internes donc 2n-2 noeuds et 2n-3 aretes
# n aretes triviales (reliant une feuille a un noeud interne)
# donc n-3 caracteres non triviaux

import sys

def newick_str(T,u):
    if isinstance(u,int): # internal node
        return '('+','.join(newick_str(T,v) for v in T[u])+')'
    else:
        return u

def main():
    S = list(input().split())
    n = len(S)
    Chars = [L.strip() for L in sys.stdin.readlines()]
    assert(len(Chars)==n-3)  # table suffisante
    Sall = frozenset(range(n))
    CharSets = set()
    for i in range(len(Chars)):
        s = frozenset(x for x in range(n) if Chars[i][x]=='1')
        CharSets.add(s)
        CharSets.add(Sall-s)
    Subsets = [frozenset({i}) for i in range(n)]
    Groups = set(range(n))
    Q = []
    for i in range(n):
        for j in range(i+1,n):
            if frozenset({i,j}) in CharSets:
                Q.append((i,j))
    N = n
    T = {}
    while len(Groups)>2:
        assert(Q)
        i,j = Q.pop()
        Subsets.append(Subsets[i]|Subsets[j])
        assert(len(Subsets)==N+1)
        T[N] = [(S[i] if i<n else i), (S[j] if j<n else j)]
        Groups.remove(i)
        Groups.remove(j)
        for k in Groups:
            if Subsets[k]|Subsets[N] in CharSets:
                Q.append((k,N))
                break
        Groups.add(N)
        N += 1
    i,j = Groups
    T[i].append(j)
    print(newick_str(T,i)+';')

main()
