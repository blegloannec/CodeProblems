#!/usr/bin/env python3

# on cherche un mot de la forme 5^a3^b
# avec a+b = N, 3|a, 5|b et a maximal
# soit R = N%3
# on cherche le plus petit k tel que 5 | R+3k
# k = (-R) * 3^(-1) mod 5 = -2R mod 5

# O(N) naive approach, good enough here
# (and actually O(1) when a solution exists due to
#  the previous analysis)
def decent(N):
    for b in range(0,N+1,5):
        a = N-b
        if a%3==0:
            return '5'*a + '3'*b
    return -1

# O(1) solution (but actually also O(N) due to the
# solution construction)
def more_decent(N):
    R = N%3
    k = (-2*R)%5
    b = R+3*k
    return '5'*(N-b)+'3'*b if b<=N else -1

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(more_decent(N))

main()
