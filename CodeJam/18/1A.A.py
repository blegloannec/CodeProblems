#!/usr/bin/env python3

def case():
    RChips = [sum(L) for L in G]
    Chips = sum(RChips)
    if Chips==0:
        return True
    Units = (H+1)*(V+1)
    if Chips%Units!=0:
        return False
    ChipsUnit = Chips//Units
    # Row separators
    ChipsR = ChipsUnit*(V+1)
    curr = 0
    RSep = [0]
    for i in range(R):
        curr += RChips[i]
        if curr>ChipsR:
            return False
        elif curr==ChipsR:
            RSep.append(i+1)
            curr = 0
    if curr:
        return False
    # Column separators
    LChips = [sum(G[i][j] for i in range(R)) for j in range(C)]
    ChipsC = ChipsUnit*(H+1)
    curr = 0
    CSep = [0]
    for i in range(C):
        curr += LChips[i]
        if curr>ChipsC:
            return False
        elif curr==ChipsC:
            CSep.append(i+1)
            curr = 0
    if curr:
        return False
    # Checking each waffle
    for i in range(len(RSep)-1):
        i0,i1 = RSep[i],RSep[i+1]
        for j in range(len(CSep)-1):
            j0,j1 = CSep[j],CSep[j+1]
            if sum(G[k][l] for l in range(j0,j1) for k in range(i0,i1))!=ChipsUnit:
                return False
    return True

def main():
    global R,C,H,V,G
    T = int(input())
    for t in range(1,T+1):
        R,C,H,V = map(int,input().split())
        G = [[int(c=='@') for c in input()] for _ in range(R)]
        print('Case #%d: %sPOSSIBLE' % (t,('' if case() else 'IM')))

main()
