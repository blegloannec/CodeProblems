#!/usr/bin/env python3

def neigh(d):
    x,y = divmod(d-1,3)
    for i in range(max(0,x-1),min(2,x+1)+1):
        for j in range(max(0,y-1),min(2,y+1)+1):
            if (i,j)!=(x,y):
                yield 3*i+j+1

memo = {}
def win(n,d):
    if n<0:
        return True
    if (n,d) not in memo:
        memo[n,d] = any(not win(n-e,e) for e in neigh(d))
    return memo[n,d]

# NB: for any N>=66, the first player only has to play any corner
#     (which obviously forbids his opponent to play a corner in the next turn)
#     for any N>=12, the first player can simply play 1
#for n in range(100):
#    print(n,''.join('#' if not win(n-d,d) else ' ' for d in range(1,10)))

n = int(input())
print(*(d for d in range(1,10) if not win(n-d,d)))
