#!/usr/bin/env python3

def sig(W):
    S = {}
    SW = []
    for c in W:
        if c not in S:
            S[c] = len(S)
        SW.append(S[c])
    return tuple(SW)

def load_dict():
    D = {}
    F = open('dictionary.lst','r')
    for L in F.readlines():
        w = L.strip().lower()
        s = sig(w)
        if s not in D:
            D[s] = [w]
        else:
            D[s].append(w)
    F.close()
    return D

def update(S0,w1,w2):
    S = S0.copy()
    for a,b in zip(w1,w2):
        if a in S and S[a]!=b:
            return None
        else:
            S[a] = b
    return S

def backtrack(S0,i=0):
    if i==len(Words):
        return S0
    for w in Dict[Sigs[i]]:
        S = update(S0,Words[i],w)
        if S is not None:
            Sol = backtrack(S,i+1)
            if Sol is not None:
                return Sol
    return None

def main():
    global Dict,Words,Sigs
    Dict = load_dict()
    Words = input().split()
    Sigs = [sig(w) for w in Words]
    O = sorted(range(len(Words)), key=(lambda i: len(Dict[Sigs[i]])))
    S = backtrack({})
    print(*(''.join(S[c] for c in w) for w in Words))

main()
