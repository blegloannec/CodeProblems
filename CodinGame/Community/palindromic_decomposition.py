#!/usr/bin/env python3

# O(N^2) approach (for both detection & counting parts)

# the following detection part could be sped up in O(N) using Manacher
# (however this is not required)
def dp_pal():
    DP = [[True]*(N+1) for _ in range(N+1)]
    for l in range(2,N+1):
        for i in range(N-l+1):
            j = i+l
            DP[i][i+l] = S[i]==S[i+l-1] and DP[i+1][i+l-1]
    return DP

if __name__=='__main__':
    S = input()
    N = len(S)
    DP = dp_pal()
    cpt = 0
    for i in range(N+1):
        if DP[0][i]:
            for j in range(i,N+1):
                if DP[i][j] and DP[j][N]:
                    cpt += 1
    print(cpt)
