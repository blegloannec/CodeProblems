#!/usr/bin/env python3

##### BEGIN DLX #####
class Cell:
    def __init__(self, horiz, verti, S, C):
        self.S = S
        self.C = C
        if horiz:
            self.L = horiz.L
            self.R = horiz
            self.L.R = self
            self.R.L = self
        else:
            self.L = self
            self.R = self
        if verti:
            self.U = verti.U
            self.D = verti
            self.U.D = self
            self.D.U = self
        else:
            self.U = self
            self.D = self

    def hide_verti(self):
        self.U.D = self.D
        self.D.U = self.U

    def unhide_verti(self):
        self.D.U = self
        self.U.D = self

    def hide_horiz(self):
        self.L.R = self.R
        self.R.L = self.L

    def unhide_horiz(self):
        self.R.L = self
        self.L.R = self

def cover(c):            # c = heading cell of the column to cover
    assert c.C is None   # must be a heading cell
    c.hide_horiz()
    i = c.D
    while i != c:
        j = i.R
        while j != i:
            j.hide_verti()
            j.C.S -= 1   # one fewer entry in this column
            j = j.R
        i = i.D


def uncover(c):
    assert c.C is None
    i = c.U
    while i != c:
        j = i.L
        while j != i:
            j.C.S += 1   # one more entry in this column
            j.unhide_verti()
            j = j.L
        i = i.U
    c.unhide_horiz()

def dancing_links_enumerate(size_universe, sets):
    header = Cell(None, None, 0, None)  # building the cell structure
    col = []
    for j in range(size_universe):
        col.append(Cell(header, None, 0, None))
    for i in range(len(sets)):
        row = None
        for j in sets[i]:
            col[j].S += 1               # one more entry in this column
            row = Cell(row, col[j], i, col[j])
    sol = []
    yield from solve(header, sol)

def solve(header, sol):
    if header.R == header:     # the instance is empty => solution found
        yield sol
        return
    c = None                   # find the least covered column
    j = header.R
    while j != header:
        if c is None or j.S < c.S:
            c = j
        j = j.R
    cover(c)                   # cover this column
    r = c.D                    # try every row
    while r != c:
        sol.append(r.S)
        j = r.R                # cover elements in set r
        while j != r:
            cover(j.C)
            j = j.R
        yield from solve(header, sol)
        j = r.L                # uncover
        while j != r:
            uncover(j.C)
            j = j.L
        sol.pop()
        r = r.D
    uncover(c)
##### END DLX #####


def sol_to_str(sol):
    sol = sorted(sol)
    O = [None]*S
    for i in range(len(sol)):
        ci = i%52
        if ci<26:
            c = chr(ci + ord('A'))
        else:
            c = chr(ci-26 + ord('a'))
        for x in Sets[sol[i]]:
            O[x] = c
    return ''.join(O)

# MAIN
if __name__=='__main__':
    W,H = map(int,input().split())
    S = W*H
    G = [list(map(int,input().split())) for _ in range(H)]
    Sets = []
    for i in range(H):
        for j in range(W):
            s = G[i][j]
            if s>0:
                for h in range(1,s+1):
                    if s%h==0:
                        w = s//h
                        for x in range(max(0,i-h+1),min(i+1,H-h+1)):
                            for y in range(max(0,j-w+1),min(j+1,W-w+1)):
                                if all((x+dx,y+dy)==(i,j) or G[x+dx][y+dy]==0 for dx in range(h) for dy in range(w)):
                                    Sets.append([(x+dx)*W+y+dy for dy in range(w) for dx in range(h)])
    Sets.sort()
    Sols = list(map(sol_to_str,dancing_links_enumerate(S,Sets)))
    print(len(Sols))
    sol = min(Sols)
    for i in range(0,S,W):
        print(sol[i:i+W])
