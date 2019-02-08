#!/usr/bin/env python3

from operator import add,sub,mul

MOD = 256
Dir = {'>': (0,1), '<': (0,-1), 'v': (1,0), '^': (-1,0)}
Ops = {'+': add, '-': sub, '*': mul}

def simu(P):
    x = y = 0
    dx,dy = Dir['>']
    S = []
    str_mode = False
    Out = []
    while True:
        assert 0<=x<len(P) and 0<=y<len(P[x])
        c = P[x][y]
        if c=='"':
            str_mode = not str_mode
        elif str_mode:
            S.append(ord(c))
        elif '0'<=c<='9':
            S.append(ord(c)-ord('0'))
        elif c in Ops:
            assert len(S)>=2
            a = S.pop()
            b = S.pop()
            S.append(Ops[c](b,a) % MOD)
        elif c in Dir:
            dx,dy = Dir[c]
        elif c=='S':
            x += dx
            y += dy
        elif c=='E':
            break
        elif c=='P':
            assert S
            S.pop()
        elif c=='X':
            assert len(S)>=2
            S[-1],S[-2] = S[-2],S[-1]
        elif c=='D':
            assert S
            S.append(S[-1])
        elif c=='_':
            assert S
            dx,dy = Dir['>' if S.pop()==0 else '<']
        elif c=='|':
            assert S
            dx,dy = Dir['v' if S.pop()==0 else '^']
        elif c=='I':
            assert S
            Out.append(str(S.pop()))
        elif c=='C':
            assert S
            Out.append(chr(S.pop()))
        else:
            assert c==' '
        x += dx
        y += dy
    return ''.join(Out)

def main():
    N = int(input())
    P = [input() for _ in range(N)]
    print(simu(P))

main()
