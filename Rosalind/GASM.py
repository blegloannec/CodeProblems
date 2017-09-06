#!/usr/bin/env python3

import sys, rosalib

# NB: "for some positive integer k, the de Bruijn graph
#      consists of exactly two directed cycles."

def build_graph_cycles(DNAS,k):
    DBG = {}
    for DNA in DNAS:
        for i in range(len(DNA)-k):
            A,B = DNA[i:i+k],DNA[i+1:i+1+k]
            if A in DBG:
                if DBG[A]!=B:
                    # le degre sortant doit etre 1
                    return None
            else:
                DBG[A] = B
    # on verifie que le graphe contient 2 cycles
    Seen = set()
    Cycles = []
    for X0 in DBG:
        if X0 not in Seen:
            Seen.add(X0)
            X = DBG[X0]
            cycle = [X0[-1]]
            while X not in Seen:
                Seen.add(X)
                cycle.append(X[-1])
                if X not in DBG:
                    return None
                X = DBG[X]
            if X!=X0:
                return None
            Cycles.append(''.join(cycle))
    return Cycles if len(Cycles)==2 else None

def main():
    DNAS = set(L.strip() for L in sys.stdin.readlines())
    DNAS |= set(rosalib.revc(DNA) for DNA in DNAS)
    DNAS = list(DNAS)
    k = len(DNAS[0])
    C = None
    while C==None:
        k -= 1
        C = build_graph_cycles(DNAS,k)
    print(C[0])

main()
