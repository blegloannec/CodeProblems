#!/usr/bin/env python3

class Enemy:
    def __init__(self, x, y, hp):
        self.x, self.y = x, y
        self.hp = hp
    def pos(self):
        return (self.x,self.y)

distinf = lambda A,B: max(abs(A[0]-B[0]),abs(A[1]-B[1]))
dist1 = lambda A,B: abs(A[0]-B[0])+abs(A[1]-B[1])
target = lambda T: min((E for E in Enemies if distinf(T,E.pos())<=2),   \
                       key = (lambda E: (E.x, dist1(T,E.pos()), -E.y)), \
                       default = None)

if __name__=='__main__':
    W,H = map(int,input().split())
    Towers = []
    Enemies = []
    for i in range(H):
        L = input()
        for j in range(W):
            if L[j]=='T':
                Towers.append((i,j))
            elif L[j]!='.':
                Enemies.append(Enemy(i,j,int(L[j])))
    R = 0
    while Enemies and all(E.x>=0 for E in Enemies):
        Enemies = [E for E in Enemies if E.pos() not in Towers]
        for T in Towers:
            E = target(T)
            if E:
                E.hp -= 1
        Enemies = [E for E in Enemies if E.hp>0]
        for E in Enemies:
            E.x -= 1
        R += 1
    print('LOSE' if Enemies else 'WIN', R)
