#!/usr/bin/env python3

S = 8
inside = lambda i,j: 0<=i<S and 0<=j<S
color = lambda c: 0 if c.isupper() else 1

DV = {'P': (((-1,-1),(-1,+1)),((+1,-1),(+1,+1))),                             \
      'N': ((-2,-1),(-2,+1),(-1,-2),(-1,+2),(+1,-2),(+1,+2),(+2,-1),(+2,+1)), \
      'K': ((-1,-1),(-1, 0),(-1,+1),( 0,-1),( 0,+1),(+1,-1),(+1, 0),(+1,+1)), \
      'B': ((-1,-1),(-1,+1),(+1,-1),(+1,+1)),                                 \
      'R': ((-1, 0),( 0,-1),( 0,+1),(+1, 0))}
DV['Q']= DV['B'] + DV['R']

def winner(Board):
    Attack = [[[False]*S for _ in range(S)] for _ in range(2)]
    King = [None]*2
    for i in range(S):
        for j in range(S):
            if Board[i][j]!='.':
                c = color(Board[i][j])
                A = Attack[c]
                p = Board[i][j].upper()
                if p in 'PNK':
                    D = DV[p][c] if p=='P' else DV[p]
                    if p=='K':
                        King[c] = (i,j)
                    for di,dj in D:
                        vi = i+di; vj = j+dj
                        if inside(vi,vj):
                            A[vi][vj] = True
                else:
                    attack_through = '.' + 'kK'[c]
                    for di,dj in DV[p]:
                        vi = i+di; vj = j+dj
                        while inside(vi,vj):
                            A[vi][vj] = True
                            if Board[vi][vj] not in attack_through:
                                break
                            vi += di; vj += dj
    for w in range(2):
        i,j = King[w^1]
        if Attack[w][i][j]:
            V = ((i+di,j+dj) for di,dj in DV['K'])
            if all(Attack[w][vi][vj] for (vi,vj) in V if inside(vi,vj) \
                   and (Board[vi][vj]=='.' or color(Board[vi][vj])==w)):
                return 'WB'[w]
    return 'N'

Board = [input() for _ in range(S)]
print(winner(Board))
