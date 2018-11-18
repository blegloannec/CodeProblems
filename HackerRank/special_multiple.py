#!/usr/bin/env python3

# we use a DP approach in O(N*S) where S = size of the solution (unknown)
# that works well for numbers up to ~10**6

# NB: the editorial uses a O(2^S) enumeration of 0/9-numbers until
# a solution is found
# that works well on the small inputs of this problem,
# but would fail on more serious inputs (e.g. N = 1000009)

# DP[s][r] = nb of 0/9-numbers x of size s such that x mod N = r
def dp(N):
    DP = [[0]*N]
    DP[0][0] = 1
    D = [9]       # digits D[k] = 9*10^k mod N
    while DP[-1][0]<2:
        DP.append([DP[-1][n]+DP[-1][(n-D[-1])%N] for n in range(N)])
        D.append((10*D[-1]) % N)
    # going backward to build the solution
    Sol = ['9']
    i = len(DP)-2
    n = (-D[i]) % N
    while i>0:
        if DP[i-1][n]>0:
            Sol.append('0')
        else:
            Sol.append('9')
            n = (n-D[i-1]) % N
        i -= 1
    return ''.join(Sol)

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(dp(N))

main()
