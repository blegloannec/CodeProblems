#!/usr/bin/env python

# https://en.wikipedia.org/wiki/Addition-chain_exponentiation
# https://oeis.org/A003313
# sans surprise, pas de prog dyn possible ici (absence de
# sous-structure optimale, l'exemple de 15 utilise un calcul non-optimal
# de 6)

# solution adoptee : backtracking (sans memoire)
# car apres essai, un bfs dans l'espace des chaines
# demande trop de memoire ici

N = 200
pmax = 12
M = [n-1 for n in xrange(N+1)]
M[0] = M[1] = 0

def backtrack(E):
    n = len(E)
    if n>=pmax:
        return
    for e in E:
        s = E[-1]+e
        if s>N:
            break
        if n<M[s]:
            M[s] = n
        E.append(s)
        backtrack(E)
        E.pop()

def main():
    backtrack([1])
    print sum(M)

main()
