#!/usr/bin/env python3

Dig = ('       __ __                        _ _           _ _           _ _ ',
       '  |      |      |     /|\   \ | /  \ | /  | | |  | | |  | | |  | | |',
       '  |      |    __|__  / | \   \|/    \|/   | | |  | | |  |_|_|  |_|_|',
       '  |      |      |      |      |      |      |      |      |      |  ',
       '  |      |    __|__    |      |      |      |      |     _|_    _|_ ',
       '  |      |      |    \ | /   /|\    /|\   | | |  | | |  | | |  | | |',
       '  |    __|__    |     \|/   / | \  /_|_\  | | |  |_|_|  | | |  |_|_|')

def cis2int(Cis, off=0):
    a = b = c = d = 0
    while any(Cis[i][off+3:off+5]!=Dig[i][7*d+3:7*d+5] for i in range(0,3)): d += 1
    while any(Cis[i][off  :off+2]!=Dig[i][7*c  :7*c+2] for i in range(0,3)): c += 1
    while any(Cis[i][off+3:off+5]!=Dig[i][7*b+3:7*b+5] for i in range(4,7)): b += 1
    while any(Cis[i][off  :off+2]!=Dig[i][7*a  :7*a+2] for i in range(4,7)): a += 1
    return 1000*a + 100*b + 10*c + d

def int2cis(n):
    n,d = divmod(n, 10)
    n,c = divmod(n, 10)
    a,b = divmod(n, 10)
    C = []
    for i in range(0,4): C.append(Dig[i][7*c:7*c+3] + Dig[i][7*d+3:7*d+5])
    for i in range(4,7): C.append(Dig[i][7*a:7*a+3] + Dig[i][7*b+3:7*b+5])
    return C

def main():
    I = [input() for _ in range(7)]
    n = sum(cis2int(I, k) for k in range(0, len(I[0]), 7)) % 10000
    Out = [L for L in map(str.rstrip, int2cis(n)) if L]
    l = min(next(i for i in range(len(L)) if L[i]!=' ') for L in Out)
    for L in Out:
        print(L[l:])

main()
