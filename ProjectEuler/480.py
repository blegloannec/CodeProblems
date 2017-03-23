#!/usr/bin/env python3

# analogue au pb 442, sauf que l'on utilise une prod. dyn.
# pour compter et non un automate

S = 'thereisasyetinsufficientdataforameaningfulanswer'

def binom(n,p):
    return 1 if p==0 else n*binom(n-1,p-1)//p

# compte les mots de taille n ecrits avec les lettres de V[0:i+1]
# la lettre i etant disponible en V[i] exemplaires
def dp(V,memo,n,i):
    if n==0: # mot complet
        return 1
    if i<0: # fail
        return 0
    if (n,i) in memo:
        return memo[n,i]
    res = 0
    for v in range(min(n,V[i])+1):
        # on choisit v positions d'insertion parmi n
        res += binom(n,v)*dp(V,memo,n-v,i-1)
    memo[n,i] = res
    return res

# compte les mots de taille <=n
def cpt(V,n):
    res = 0
    memo = {}
    for v in range(n): # blancs a la fin
        res += dp(V,memo,n-v,len(V)-1)
    return res

def W(V0,p):
    V = V0[:] # copie
    p0,l,res = 0,14,[]
    while p0<p:
        for a in range(len(V)):
            if V[a]>0:
                V[a] -= 1 # on commence par la lettre a
                p0 += 1 # pour compter la lettre seule
                psvg = p0
                p0 += cpt(V,l)
                if p0>p:
                    # on a trouve une nouvelle lettre
                    p0 = psvg
                    res.append(chr(a+ord('a')))
                    break
                V[a] += 1
        l -= 1 # on reduit la taille du suffixe recherche
    return ''.join(res)

def P(V0,w):
    V = V0[:] # copie
    l,res = 14,0
    for a in w:
        a = ord(a)-ord('a')
        for a0 in range(a):
            if V[a0]>0:
                V[a0] -= 1
                res += cpt(V,l)+1
                V[a0] += 1
        assert(V[a]>0) # sinon le mot n'est pas dans la liste
        V[a] -= 1
        l -= 1
        res += 1
    return res

def main():
    V = [0]*26
    for s in S:
        V[ord(s)-ord('a')] += 1
    print(W(V,P(V,'legionary')+P(V,'calorimeters')-P(V,'annihilate')+P(V,'orchestrated')-P(V,'fluttering')))

main()
