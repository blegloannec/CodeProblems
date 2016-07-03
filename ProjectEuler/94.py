#!/usr/bin/env python

# x la longueur des 2 cotes egaux, y = x +/- 1 le 3eme cote
# h la hauteur, h^2 = x^2 - (y/2)^2
# il faut une aire A = h*y/2 entiere, donc h*y entier pair
# 1. Cas y = x+1
# h^2 = x^2 - 1/4 * (x+1)^2
# (2h)^2 = 3x^2 - 2x - 1
# 3(2h)^2 = (3x-1)^2 - 4
# (3x-1)^2 - 3(2h)^2 = 4
# on redivise finalement par 4 pour avoir une equation de Pell :
# X^2 - 3*h^2 = 1, X = (3x-1)/2
# 2. Cas y = x-1
# on aboutit a la meme equation :
# X^2 - 3*h^2 = 1, X = (3x+1)/2

def main():
    # solution fondamentale pour D = 3
    # ne compte pas car correspondrait a la fausse solution
    # x = 1, y = 0
    X0,H0 = 2,1
    X,H = X0,H0
    res = 0
    while 2*(2*X-1)/3+(2*X-1)/3-1<=10**9:
        X,H = X0*X + 3*H0*H, X0*H + H0*X
        if (2*X-1)%3==0:
            x = (2*X-1)/3
            y = x-1
            if (y*H)%2==0:
                if 2*x+y<=10**9:
                    res += 2*x+y
        if (2*X+1)%3==0:
            x = (2*X+1)/3
            y = x+1
            if (y*H)%2==0:
                if 2*x+y<=10**9:
                    res += 2*x+y
    print res

main()
