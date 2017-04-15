#!/usr/bin/env python3

# O((NP)^2)
def greedy(I):
    cpt = 0
    while True:
        n0 = 0 # package avec la plus petite limite de fin
        # intersection des intervalles des packages courants
        intl,intr = -float('inf'),float('inf')
        for n in range(len(I)):
            if not I[n]: # l'ingredient n n'a plus de packages
                return cpt
            if I[n][-1][1]<I[n0][-1][1]:
                n0 = n
            # intersection
            intl = max(intl,I[n][-1][0])
            intr = min(intr,I[n][-1][1])
        if intl>intr: # intersection vide
            I[n0].pop() # on retire le package qui n'a plus aucune chance
        else: # on a trouve un kit avec les packages courants
            cpt += 1
            # on les retire tous
            for n in range(len(I)):
                I[n].pop()

def main():
    T = int(input())
    for t in range(1,T+1):
        N,P = map(int,input().split())
        R = list(map(int,input().split()))
        Q,I = [],[[] for _ in range(N)]
        for n in range(N):
            Q.append(list(map(int,input().split())))
            # on ajoute les intervalles de nb de servings acceptables
            # par package
            for q in Q[n]:
                X = ((100*q+110*R[n]-1)//(110*R[n]),100*q//(90*R[n]))
                if X[0]<=X[1]: # package acceptable
                    I[n].append(X)
            # on trie par (valeur de fin, valeur de debut)
            # (et on inverse juste pour depop plus facilement)
            I[n].sort(key=(lambda x: (x[1],x[0])),reverse=True)
        print('Case #%d: %d' % (t,greedy(I)))

main()
