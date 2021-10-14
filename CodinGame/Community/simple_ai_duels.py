#!/usr/bin/env python3

# NB: As both AIs use the same RNG, they cannot actually play
#     in parallel (one has to make its random choice before).


class LCG:
    def __init__(self, x0=12):
        self.x = x0

    def __call__(self):
        self.x = (137*self.x + 187) & 255
        b = 0
        for i in range(8):
            b ^= (self.x>>i)&1
        return 'DC'[b]

RNG = LCG()


class AI:
    c = 2
    d = 1
    t = 3
    f = 0

    def __init__(self, opp=None):
        l, self.name = input().split()
        self.Prog = [input().split() for _ in range(int(l))]
        self.turn_cnt = 0
        self.Moves = []
        self.last = None
        self.reward = 0
        self.Opp = opp

    def action(self, a):
        self.last = RNG() if a=='RAND' else a

    def update(self):
        if self.last==self.Opp.last=='C':
            self.reward += self.c
        elif self.last==self.Opp.last=='D':
            self.reward += self.d
        elif self.last=='D':
            self.reward += self.t
        else:
            self.reward += self.f
        self.Moves.append(self.last)

    def turn(self):
        for L in self.Prog:
            if L[0]=='*':
                self.action(L[1])
                break
            elif L[0]=='START':
                if self.turn_cnt==0:
                    self.action(L[1])
                    break
            elif L[1]=='-1':    # OPP -1 X Y
                assert self.turn_cnt>0
                move = self.Moves[-1] if L[0]=='ME' else self.Opp.Moves[-1]
                if move==L[2]:
                    self.action(L[3])
                    break
            elif L[1]=='MAX':   # ME MAX X Y
                moves = self.Moves if L[0]=='ME' else self.Opp.Moves
                if 2*moves.count(L[2])>len(moves):
                    self.action(L[3])
                    break
            elif L[1]=='LAST':  # OPP LAST N X Y
                N = int(L[2])
                moves = self.Moves[-N:] if L[0]=='ME' else self.Opp.Moves[-N:]
                if 2*moves.count(L[3])>len(moves):
                    self.action(L[4])
                    break
            elif L[1]=='WIN':   # ME WIN Y
                comp = self.reward>self.Opp.reward if L[0]=='ME' else self.reward<self.Opp.reward
                if comp:
                    self.action(L[2])
                    break
        self.turn_cnt += 1


def main():
    N = int(input())
    A = AI()
    A.Opp = B = AI(A)
    for _ in range(N):
        A.turn()
        B.turn()
        A.update()
        B.update()
    print('DRAW' if A.reward==B.reward else A.name if A.reward>B.reward else B.name)

main()
