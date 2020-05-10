#!/usr/bin/env python3

# seeing a configuration as an alternating sequence of R/B segments,
# it is easy to:
#  - reorganize arbitrarily the sizes of these segments
#    (except when they all have size 1)
#  - remove some segments
# it's however impossible to create new segments

def main():
    N = int(input())
    S = input()
    T = input()
    s = sum(S[i]!=S[i-1] for i in range(N))
    t = sum(T[i]!=T[i-1] for i in range(N))
    possible = s>t or (s==t and 0<s<N)
    print('yes' if possible else 'no')

main()
