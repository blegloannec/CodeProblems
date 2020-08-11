#!/usr/bin/env python3

# greedy O(n) for the minimum vertex cover of a tree
# greedily remove leaves while picking the parent of each not-picked leaf

def main():
    N = int(input())
    if N==1:
        print(1)
        return
    T = [set(int(v)-1 for v in input().split()[2:]) for _ in range(N)]
    C = [False]*N
    L = [u for u in range(N) if len(T[u])==1]
    while L:
        u = L.pop()
        if T[u]:
            assert len(T[u])==1
            v = T[u].pop()
            if not C[u]:
                C[v] = True
            T[v].remove(u)
            if len(T[v])==1:
                L.append(v)
    print(sum(C))

main()
