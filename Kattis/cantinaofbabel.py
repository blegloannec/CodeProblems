#!/usr/bin/env python3

### SCC by Tarjan, tryalgo's implementation
def tarjan(graph):
    n = len(graph)
    dfs_num = [None] * n
    dfs_min = [n] * n
    waiting = []
    waits = [False] * n  # invariant: waits[v] iff v in waiting
    sccp = []          # list of detected components
    dfs_time = 0
    times_seen = [-1] * n
    for start in range(n):
        if times_seen[start] == -1:                    # initiate path
            times_seen[start] = 0
            to_visit = [start]
            while to_visit:
                node = to_visit[-1]                    # top of stack
                if times_seen[node] == 0:              # start process
                    dfs_num[node] = dfs_time
                    dfs_min[node] = dfs_time
                    dfs_time += 1
                    waiting.append(node)
                    waits[node] = True
                children = graph[node]
                if times_seen[node] == len(children):  # end of process
                    to_visit.pop()                     # remove from stack
                    dfs_min[node] = dfs_num[node]      # compute dfs_min
                    for child in children:
                        if waits[child] and dfs_min[child] < dfs_min[node]:
                            dfs_min[node] = dfs_min[child]
                    if dfs_min[node] == dfs_num[node]:  # representative
                        component = []                 # make component
                        while True:                    # add nodes
                            u = waiting.pop()
                            waits[u] = False
                            component.append(u)
                            if u == node:              # until repr.
                                break
                        sccp.append(component)
                else:
                    child = children[times_seen[node]]
                    times_seen[node] += 1
                    if times_seen[child] == -1:        # not visited yet
                        times_seen[child] = 0
                        to_visit.append(child)
    return sccp
###

from collections import defaultdict

def main():
    N = int(input())
    Speaks = [None]*N
    Understands = defaultdict(list)
    for u in range(N):
        L = input().split()
        Speaks[u] = L[1]
        for l in range(1,len(L)):
            Understands[L[l]].append(u)
    Graph = [Understands[Speaks[u]] for u in range(N)]
    Comp = tarjan(Graph)
    print(N-max(len(C) for C in Comp))

main()
