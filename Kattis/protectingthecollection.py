#!/usr/bin/env python3

# Insights:
#  - If one reflects on the additional mirror twice, then it is equivalent
#    to either reflect on the other mirror direction, or not reflect at all
#    the first time.
#    Hence remembering the position of the additional mirror is useless.
#  - If ones does a DFS to find the solution and prioritizes the exploration
#    of the natural path, then all cells that can be reached without using the
#    additional mirror (hence with that mirror still available) will be
#    explored *before* the same cells without the additional mirror available.
#    Hence there is no need to remember the availability of the mirror in
#    the seen states.

def dfs():
    key_bit = lambda di, dj: 1<<((di+1)*3 + (dj+1))  # we neglect extra
    u0 = i0, j0, di0, dj0, ex0 = 0, C, 1, 0, True
    Q = [u0]
    Seen = [[0]*N for _ in range(N)]
    Seen[0][C] |= key_bit(di0, dj0)
    while Q:
        i, j, di, dj, extra = Q.pop()
        V = []
        if G[i][j]=='.':
            # natural path first
            V.append((i+di, j+dj, di, dj, extra))
            # then using extra mirror
            if extra:  # we can freely turn left/right
                for (vdi,vdj) in ((dj,di),(-dj,-di)):
                    V.append((i+vdi, j+vdj, vdi, vdj, False))
        else:
            di,dj = (-dj,-di) if G[i][j]=='/' else (dj,di)
            V.append((i+di, j+dj, di, dj, extra))
        for v in V:
            vi, vj, vdi, vdj, _ = v
            if vi==R and vj==N:
                return True
            b = key_bit(vdi,vdj)
            if 0<=vi<N and 0<=vj<N and not Seen[vi][vj]&b:
                Seen[vi][vj] |= b
                Q.append(v)
    return False

def main():
    global N,C,R,G
    N,C,R = map(int,input().split())
    G = [input().split() for _ in range(N)]
    C -= 1
    R -= 1
    print('YES' if dfs() else 'NO')

main()
