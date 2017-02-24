#!/usr/bin/env python3

# la suite est generee par la regle de substitution suivante
# u(i) -> u(i) times x where x = A if i%2==0 else B
# generation en O(n)

N = int(input())
A,B = map(int,input().split())
U = [A]*A + [B]*(A if A>1 else B)
i = 2
while len(U)<N:
    U += [A if i%2==0 else B]*U[i]
    i += 1
print(''.join(map(str,U[:N])))
