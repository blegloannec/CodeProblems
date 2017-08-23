#!/usr/bin/env python3

import sys

# lazy hack du parser de NWCK

def is_letter(a):
    return 'a'<=a<='z' or 'A'<=a<='Z' or '0'<=a<='9' or a in '_:'

def parse_newick(L,T):
    S = []
    curr_name = []
    curr_children = []
    for i in range(len(L)):
        if L[i]=='(':
            assert(not curr_name)
            S.append('(')
        elif L[i] in '),;':
            if not curr_name:
                name = 'node%d'%(len(T))
                dist = None
            else:
                distsep = curr_name.index(':')
                name = ''.join(curr_name[:distsep])
                dist = int(''.join(curr_name[distsep+1:]))
                if name=='':
                    name = 'node%d'%(len(T))
            T[name] = curr_children
            S.append((name,dist))
            curr_children = []
            if L[i]==')':
                while S[-1]!='(':
                    curr_children.append(S[-1])
                    S.pop()
                S.pop()
            elif L[i]==';':
                assert(len(S)==1)
                assert(isinstance(S[0],tuple))
                assert(S[0][1]==None)
                return S[0][0]
            curr_name = []
        else:
            assert(is_letter(L[i]))
            curr_name.append(L[i])

def unroot(T,u,u0=None,d=0):
    for (v,w) in T[u]:
        assert(v!=u0)
        unroot(T,v,u,w)
    if u0!=None:
        T[u].append((u0,d))

def tree_dist_dfs(T,Dist,u,u0=None):
    for (v,w) in T[u]:
        if v!=u0:
            Dist[v] = Dist[u]+w
            tree_dist_dfs(T,Dist,v,u)

def main():
    L = sys.stdin.readlines()
    res = []
    for i in range(0,len(L),3):
        NW = L[i].strip  ()
        T = {}
        root = parse_newick(NW,T)
        unroot(T,root)
        u,v = L[i+1].split()
        D = {u:0}
        tree_dist_dfs(T,D,u)
        res.append(D[v])
    print(' '.join(map(str,res)))

main()
