#!/usr/bin/env python3

# adding lines one-by-one, each line creates x+1 new pieces,
# for x the number of intersections inside the circle of this
# line with the previous ones

def separated():
    for i in range(N):
        xi,yi = Cndl[i]
        for j in range(i+1,N):
            xj,yj = Cndl[j]
            if all((a*xi+b*yi+c)*(a*xj+b*yj+c)>0 for a,b,c in Line):
                return False
    return True

def faces():
    res = M+1
    for i in range(M):
        ai,bi,ci = Line[i]
        for j in range(i):
            aj,bj,cj = Line[j]
            d = ai*bj-aj*bi
            if d!=0:  # intersection
                x = (-ci*bj+cj*bi)/d
                y = (-ci*aj+cj*ai)/d
                if x*x+y*y<R*R:
                    res += 1
    return res

def main():
    global N, Cndl, M, Line, R
    N,M,R = map(int, input().split())
    Cndl = [tuple(map(int, input().split())) for _ in range(N)]
    Line = [tuple(map(int, input().split())) for _ in range(M)]
    print('yes' if separated() and faces()==N else 'no')

main()
