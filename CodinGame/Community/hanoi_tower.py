#!/usr/bin/env python3

N = int(input())
T = int(input())

# Move sequence
S = [list(range(N,0,-1)),[],[]]
s = 0 # smallest disk position
for t in range(T):
    if t%2==0: # smallest disk move
        ns = (s+1)%3 if N%2==0 else (s-1)%3
        S[ns].append(S[s].pop())
        s = ns
    else:
        O = sorted([(S[x%3][-1] if S[x%3] else float('inf'),x%3) for x in [s+1,s+2]])
        S[O[1][1]].append(S[O[0][1]].pop())

# Printing
D = [[' ']*(8*N) for _ in range(N)]
P = [N,3*N+2,5*N+4]
for i in range(3):
    for j in range(N):
        j0 = N-1-j
        if j0<len(S[i]):
            for x in range(-S[i][j0],S[i][j0]+1):
                D[j][P[i]+x] = '#'
        else:
            D[j][P[i]] = '|'
for L in D:
    print(''.join(L).rstrip())

print(2**N-1)
