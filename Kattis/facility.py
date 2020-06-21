#!/usr/bin/env python3

import sys
input = sys.stdin.readline

# consider the facilities/clients bipartite graph
# where edges are the 0 coefficients of the matrix
# we want a set of <= k facilities that cover all the clients
# the special property implies that:
#   f~{c,c'} & f'~c  =>  f'~c'
# implying that connected components of the graph
# are bipartite cliques, hence one facility is enough
# to cover all the clients of the component

def main():
    M,N,K = map(int, input().split())
    Cov = [False]*N
    Cnt = 0
    for _ in range(M):
        pick = False
        for c,v in enumerate(input().split()):
            if v=='0' and not Cov[c]:
                Cov[c] = pick = True
        if pick:
            Cnt += 1
    print('yes' if all(Cov) and Cnt<=K else 'no')

main()
