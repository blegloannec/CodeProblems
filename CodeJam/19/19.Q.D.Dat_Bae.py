#!/usr/bin/env python3

import sys

# The following strategy uses only F = 4:
#  - Group nodes by blocks of 2**F = 16 nodes.
#    Node i is numbered i%16 in block i//16.
#  - At query 0<=q<4, send to each node the q-th bit of its number.
#    After all queries, each non-broken node has echoed its number
#    within its block.
#  - As the number of broken nodes B < 16 the size of a block,
#    it is impossible to skip a whole block and hence is easy
#    to deduce the blocks of the received numbers, thus retrieving
#    working nodes.
# (NB: for the small dataset, F = 10 which is enough to send its full
#      number to each node.)

F = 4           # 4 queries is enough for <16 broken nodes
BS = (1<<F)-1   # block mask (2^F-1 = 15) for blocks of size 2^F = 16
NMAX = 1<<10
Queries = [''.join(str((i>>b)&1) for i in range(NMAX)) for b in range(F)]

def send_recv(S):
    print(S)
    sys.stdout.flush()
    return input()

def case():
    N,_,_ = map(int,input().split())
    # send/recv queries
    Raw = [list(map(int,send_recv(Queries[i][:N]))) for i in range(F)]
    # gathering received numbers
    Num = [sum(Raw[b][j]<<b for b in range(F)) for j in range(len(Raw[0]))]
    # extracting broken nodes
    j = 0
    Res = []
    for i in range(N):
        if j<len(Num) and Num[j]==i&BS:
            j += 1
        else:
            Res.append(i)
    assert send_recv(' '.join(map(str,Res)))=='1'

if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        case()
