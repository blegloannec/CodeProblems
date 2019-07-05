#!/usr/bin/env python3

# having fun doing it the most convoluted possible way, enumerating
# the "hand" exact covers by "pairs" and "sets" using dancing links

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
    for i, _ in enumerate(sets):
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

if __name__=='__main__':
    A,B = input().split()
    H = A+B
    curr = None
    Hand = []
    for c in reversed(H):
        if '1'<=c<='9':
            Hand.append((curr,int(c)))
        else:
            curr = c
    Hand.sort()
    Size = len(Hand)
    # kokushi musou
    Ref = (('m',1),('m',9),('p',1),('p',9),('s',1),('s',9),('z',1),('z',2),('z',3),('z',4),('z',5),('z',6),('z',7))
    iref = 0
    win = True
    for c in Hand:
        if c==Ref[iref]:
            iref += 1
        elif c not in Ref:
            win = False
            break
    win |= iref==len(Ref)
    if not win:
        Sets = []
        # gen "pairs"
        for i in range(Size-1):
            if Hand[i]==Hand[i+1]:
                Sets.append((i,i+1))
        # gen "sets" (kinda naively...)
        for i in range(Size):
            for j in range(i+1,Size):
                for k in range(j+1,Size):
                    if Hand[i]==Hand[j]==Hand[k] or \
                       (Hand[i][0]==Hand[j][0]==Hand[k][0]!='z' and Hand[i][1]==Hand[j][1]-1==Hand[k][1]-2):
                        Sets.append((i,j,k))
        # enumerating solutions
        for Sol in dancing_links_enumerate(Size, Sets):
            if sum(1 for s in Sol if len(Sets[s])==3)==4 or \
               (len(Sol)==7 and len(set(Hand[Sets[s][0]] for s in Sol))==7):
                win = True
                break
    print(str(win).upper())
