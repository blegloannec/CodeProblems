#!/usr/bin/env python

# similaire au pb 94
# on avait cependant pour ce dernier pousse l'analyse
# plus loin qu'ici (on avait cherche a se ramener a une equation
# de Pell, et pas simplement a une equation diophantienne
# quadratique generale, ce dont on se contentera ici...)

# h^2 = L^2 - (b/2)^2, soit 4h^2 = 4L^2 - b^2
# pour h = b +/- 1, on trouve 5b^2 +/- 8b + 4 - 4L^2 = 0
# equation diophantienne quadratique, on utilise le solveur
# https://www.alpertron.com.ar/JQUAD.HTM
# pour obtenir les coeff de generation des solutions
# l'enonce du pb nous donne de plus une (la seule ?) solution
# fondamentale pour chacun des 2 cas, ce qui est suffisant pour
# generer les 12 premiers triangles

def main():
    # les solutions fondamentales sont donnes par l'enonce
    # (il y en a peut-etre d'autres, mais elles ne sont pas
    # necessaires pour generer les 12 plus petits triangles)
    Fond0 = [(272,305)] # pour h = b+1
    Fond1 = [(16,17)]   # pour h = b-1
    sol = []
    for (b0,L0) in Fond0:
        b,L = b0,L0
        sol0 = [L]
        while len(sol0)<12:
            b,L = -9*b-8*L-8,-10*b-9*L-8
            #assert(4*L*L-b*b==4*(b+1)**2)
            if L>0:
                sol0.append(L)
        sol += sol0
    for (b0,L0) in Fond1:
        b,L = b0,L0
        sol0 = [L]
        while len(sol0)<12:
            b,L = -9*b-8*L+8,-10*b-9*L+8
            #assert(4*L*L-b*b==4*(b-1)**2)
            if L>0:
                sol0.append(L)
        sol += sol0
    sol.sort()
    print sum(sol[:12])

main()
