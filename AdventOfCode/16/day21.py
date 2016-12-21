#!/usr/bin/env python

import sys

P = [L.split() for L in sys.stdin.readlines()]

# fast coding, some dirty bits, yet good enough
# for such a problem...

# Part One
def scramble(S):
    for I in P:
        if I[0]=='swap':
            if I[1]=='position':
                X,Y = int(I[2]),int(I[5])
                S[X],S[Y] = S[Y],S[X]
            else:
                X,Y = I[2],I[5]
                S = map(lambda s: Y if s==X else X if s==Y else s, S)
        elif I[0]=='rotate':
            if I[1]=='left':
                X = int(I[2])
                S = [S[(i+X)%len(S)] for i in xrange(len(S))]
            elif I[1]=='right':
                X = int(I[2])
                S = [S[(i-X)%len(S)] for i in xrange(len(S))]
            else:
                X = I[6]
                x = S.index(X)
                S = [S[(i-1-x-int(x>=4))%len(S)] for i in xrange(len(S))]
        elif I[0]=='reverse':
            X,Y = int(I[2]),int(I[4])
            S = S[:X]+S[X:Y+1][::-1]+S[Y+1:]
        else:
            X,Y = int(I[2]),int(I[5])
            x = S[X]
            S = S[:X]+S[X+1:]
            S = S[:Y]+[x]+S[Y:]
    return ''.join(S)

print scramble(list('abcdefgh'))


# Part Two
def unscramble(S):
    for I in reversed(P):
        if I[0]=='swap':
            if I[1]=='position':
                X,Y = int(I[2]),int(I[5])
                S[X],S[Y] = S[Y],S[X]
            else:
                X,Y = I[2],I[5]
                S = map(lambda s: Y if s==X else X if s==Y else s, S)
        elif I[0]=='rotate':
            if I[1]=='left':
                X = int(I[2])
                S = [S[(i-X)%len(S)] for i in xrange(len(S))]
            elif I[1]=='right':
                X = int(I[2])
                S = [S[(i+X)%len(S)] for i in xrange(len(S))]
            else: # seul cas difficile
                X = I[6]
                # on essaye betement tous les x
                for x in xrange(len(S)):
                    S0 = [S[(i+1+x+int(x>=4))%len(S)] for i in xrange(len(S))]
                    if S0.index(X)==x:
                        S = S0
                        break
        elif I[0]=='reverse':
            X,Y = int(I[2]),int(I[4])
            S = S[:X]+S[X:Y+1][::-1]+S[Y+1:]
        else:
            Y,X = int(I[2]),int(I[5])
            x = S[X]
            S = S[:X]+S[X+1:]
            S = S[:Y]+[x]+S[Y:]
    return ''.join(S)

print unscramble(list('fbgdceah'))
