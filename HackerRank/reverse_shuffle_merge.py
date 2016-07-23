#!/usr/bin/env python

import sys

def valid(curr,req):
    for i in xrange(26):
        if curr[i]<req[i]:
            return False
    return True

# algo glouton O(n^2)
def main_quad():
    S = map((lambda x: ord(x)-ord('a')),sys.stdin.readline().strip())[::-1]
    curr = [0 for _ in xrange(26)]
    for c in S:
        curr[c] += 1
    # curr est le tableau des lettres restantes (dans le suffixe courant)
    req = map((lambda x: x/2),curr) # tableau des lettres requises (dans le suffixe courant)
    req_size = sum(req)
    pos = 0 # debut du suffixe courant
    sol = [] # solution partielle
    while len(sol)<req_size:
        best_pos = None
        for i in xrange(pos,len(S)):
            # on va chercher dans le suffixe courant la plus petite lettre encore requise
            # et telle que le suffixe commencant en cette lettre contienne au moins toutes les
            # lettres encore requises
            if not valid(curr,req):
                break
            if req[S[i]]>0 and (best_pos==None or S[i]<S[best_pos]):
                best_pos = i
                best_curr = curr[:]
            curr[S[i]] -= 1
        pos = best_pos+1
        sol.append(S[best_pos])
        curr = best_curr
        curr[S[best_pos]] -= 1
        req[S[best_pos]] -= 1
    print ''.join(map((lambda x: chr(x+ord('a'))),sol))

# algo glouton lineaire
# O(n * sigma^2) pour sigma la taille de l'alphabet (constante)
def main_lin():
    S = map((lambda x: ord(x)-ord('a')),sys.stdin.readline().strip())[::-1]
    # Pre-calcul lineaire O(n*sigma) :
    # - remaining[i] contient le vecteur du nombre d'occurrences de chaque lettre
    #   dans le suffixe commencant en position i
    # - next_letters[i] contient le vecteur des positions de la premiere occurrence
    #   de chaque lettre dans le suffixe commencant en position i
    remaining = [[] for _ in xrange(len(S))]
    cpt = [0 for _ in xrange(26)]
    next_letters = [[] for _ in xrange(len(S))]
    curr_next = [None for _ in xrange(26)]
    for i in xrange(len(S)-1,-1,-1):
        cpt[S[i]] += 1
        remaining[i] = cpt[:]
        curr_next[S[i]] = i
        next_letters[i] = curr_next[:]
    req = map((lambda x: x/2),cpt) # tableau des lettres requises (dans le suffixe courant)
    req_size = sum(req)
    pos = 0 # debut du suffixe courant
    sol = [] # solution partielle
    while len(sol)<req_size:
        # on va tester, dans le suffixe courant, pour chaque lettre de l'alphabet encore requise
        # (considerees dans l'ordre lex), si le suffixe commencant en la premiere occurrence
        # de cette lettre contient au moins toutes les lettres requises, si oui on prend la lettre
        # et on recommence avec pour suffixe courant le suffixe commencant apres cette lettre
        for c in xrange(26):
            if req[c]>0 and valid(remaining[next_letters[pos][c]],req):
                pos = next_letters[pos][c]+1
                sol.append(c)
                req[c] -= 1
                break
    print ''.join(map((lambda x: chr(x+ord('a'))),sol))

main_lin()
