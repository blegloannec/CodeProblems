#!/usr/bin/env python3

class Awale:
    def __init__(self, op_bowls, my_bowls):
        self.bowls = my_bowls+op_bowls

    def my_play(self, i):
        assert(0<=i<6)
        g = self.bowls[i]
        q,r = divmod(g,13)
        self.bowls[i] = 0
        for j in range(min(13,g)):
            self.bowls[(i+j+1)%13] += q + int(j<r)
        return (i+g)%13==6

    def __str__(self):
        return ' '.join(map(str,self.bowls[7:13])) + ' [%d]\n'%self.bowls[13] +' '.join(map(str,self.bowls[:6])) + ' [%d]'%self.bowls[6]

def main():
    op_bowls = list(map(int,input().split()))
    my_bowls = list(map(int,input().split()))
    A = Awale(op_bowls,my_bowls)
    num = int(input())
    rep = A.my_play(num)
    print(A)
    if rep:
        print('REPLAY')

main()
