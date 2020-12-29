#!/usr/bin/env python3

# Interactive problem!

import sys

recv = sys.stdin.readline

def send(s):
    sys.stdout.write(s)
    if not s or s[-1]!='\n':
        sys.stdout.write('\n')
    sys.stdout.flush()

def send_recv(s):
    send(s)
    return recv()

def main():
    N = int(recv())
    # number of neighbors of each vertex in N queries
    V = [int(send_recv(f'? 1 {u}')) for u in range(1, N+1)]
    # request pairs to guess each edge in N(N-1)/2 queries
    E = [[0]*N for _ in range(N)]
    for u in range(1, N+1):
        for v in range(u+1, N+1):
            Quv = int(send_recv(f'? 2 {u} {v}'))
            # Quv = Vu + Vv     if no (u,v) edge
            #     = Vu + Vv - 2 otherwise
            if Quv != V[u-1]+V[v-1]:
                E[u-1][v-1] = E[v-1][u-1] = 1
    send('!')
    for L in E:
        send(' '.join(map(str, L)))

main()
