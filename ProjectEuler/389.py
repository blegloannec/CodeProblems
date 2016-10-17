#!/usr/bin/env python

# 1 <= T <= 4
# 1 <= C <= 6*Tmax = 24
# 1 <= O <= 8*Cmax = 192
# 1 <= D <= 12*Omax = 2304
# 1 <= I <= 20*Dmax = 46080

# E(I) = sum( E(I|D=d)*P(D=d), d=1..Dmax )
# E(I|D=d) = E( sum( Xi, i=1..d ) )
# pour Xi la valeur du ieme de
#          = sum( E(Xi), i=1..d ) par linearite de E
# pour tout i, E(Xi) = (1+2+...+20)/20 = (1+20)/2, note E(X)
#          = d*E(X)
# E(I) = E(X) * sum( d*P(D=d), d=1..Dmax )
#      = E(X) * E(D)

# E(I^2) = sum( E(I^2|D=d)*P(D=d), d=1..Dmax )
# E(I^2|D=d) = E( sum( Xi, i=1..d )^2 )
#            = E( sum( Xi^2, i=1..d) + 2*sum( Xi*Xj, 1<=i<j<=d ) )
#            = sum( E(Xi^2), i=1..d ) + 2*sum( E(Xi*Xj), 1<=i<j<=d ) par linearite de E
# pour tout i, E(Xi^2) = (1^2+2^2+...+20^2)/20 = (20+1)*(2*20+1)/6, note E(X^2)
# et pour tout i=/=j, E(Xi*Xj) = (1+2+...+20)^2/20^2 = E(X)^2
#            = d * E(X^2) + d*(d-1)/2 * 2 * E(X)^2
#            = d*E(X^2) + d^2*E(X)^2 - d*E(X)^2
#            = d*(E(X^2)-E(X)^2) + d^2*E(X)^2
#            = d*V(X) + d^2*E(X)^2
# E(I^2) = sum( E(I^2|D=d)*P(D=d), d=1..Dmax )
#        = sum( d*V(X)*P(D=d) + d^2*E(X)^2, d=1..Dmax )
#        = V(X)*E(D) + E(X)^2*E(D^2)

E,E2 = 1.,1.
for x in [4,6,8,12,20]:
    EX = (1+x)/2.
    EX2 = (x+1)*(2*x+1)/6.
    VX = EX2-EX**2
    E,E2 = EX*E, VX*E+EX**2*E2
print E2-E**2
