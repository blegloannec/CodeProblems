#!/usr/bin/env python3

# tryalgo's hungarian method implementation
def kuhn_munkres(G, TOLERANCE=1e-6):
    nU = len(G)
    U = range(nU)
    nV = len(G[0])
    V = range(nV)
    assert nU <= nV
    mu = [None] * nU                # empty matching
    mv = [None] * nV
    lu = [max(row) for row in G]    # trivial labels
    lv = [0] * nV
    for root in U:                  # build an alternate tree
        au = [False] * nU           # au, av mark nodes...
        au[root] = True             # ... covered by the tree
        Av = [None] * nV            # Av[v] successor of v in the tree
        # for every vertex u, slack[u] := (val, v) such that
        # val is the smallest slack on the constraints (*)
        # with fixed u and v being the corresponding vertex
        slack = [(lu[root] + lv[v] - G[root][v], root) for v in V]
        while True:
            ((delta, u), v) = min((slack[v], v) for v in V if Av[v] is None)
            assert au[u]
            if delta > TOLERANCE:   # tree is full
                for u0 in U:        # improve labels
                    if au[u0]:
                        lu[u0] -= delta
                for v0 in V:
                    if Av[v0] is not None:
                        lv[v0] += delta
                    else:
                        (val, arg) = slack[v0]
                        slack[v0] = (val - delta, arg)
            assert abs(lu[u] + lv[v] - G[u][v]) <= TOLERANCE  # equality
            Av[v] = u                # add (u, v) to A
            if mv[v] is None:
                break                # alternating path found
            u1 = mv[v]
            assert not au[u1]
            au[u1] = True            # add (u1, v) to A
            for v1 in V:
                if Av[v1] is None:   # update margins
                    alt = (lu[u1] + lv[v1] - G[u1][v1], u1)
                    if slack[v1] > alt:
                        slack[v1] = alt
        while v is not None:         # ... alternating path found
            u = Av[v]                # along path to root
            prec = mu[u]
            mv[v] = u                # augment matching
            mu[u] = v
            v = prec
    return (mu, sum(lu) + sum(lv))


if __name__=='__main__':
    n,m = map(int,input().split())
    while n!=0:
        M = [[-float(x) for x in input().split()] for _ in range(n)]
        for _ in range(m-n):
            M.append([0]*m)
        res = -kuhn_munkres(M)[1] / n
        print('%.2f' % round(res+1e-6,2))
        n,m = map(int,input().split())
