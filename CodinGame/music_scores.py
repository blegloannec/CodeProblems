#!/usr/bin/env python3

def decode_image():
    global W,H,P
    W,H = map(int,input().split())
    P = [[False]*W for _ in range(H)]
    I = input().split()
    p = 0
    for i in range(0,len(I),2):
        n = int(I[i+1])
        if I[i]=='B':
            for _ in range(n):
                y,x = divmod(p,W)
                P[y][x] = True
                p += 1
        else:
            p += n

# We rely on the first non empty column to identify the 5 lines.
def identify_lines():
    global Line0, HLine, DLine
    for j in range(W):
        Lines = [i for i in range(1,H) if P[i][j]!=P[i-1][j]]
        if Lines:
            assert len(Lines)==10
            Line0 = Lines[0]
            HLine = Lines[1]-Lines[0]
            DLine = Lines[2]-Lines[0]
            break

def on_a_line(i):
    return 0 <= (i-Line0)%DLine < HLine

def identify_notes():
    global Notes
    Notes = []
    noted = set()
    for j in range(W):
        for i in range(H):
            if P[i][j] and not on_a_line(i) and (i,j) not in noted:
                # DFS to identify the connected component of a note
                Q = [(i,j)]
                noted.add((i,j))
                note = set(Q)
                while Q:
                    x,y = Q.pop()
                    if on_a_line(x):
                        V = [(x-1,y),(x+1,y)]
                    else:
                        V = [(vx,vy) for vx in range(x-1,x+2) for vy in range(y-1,y+2) if (vx,vy)!=(x,y)]
                        # NB: 8-connected neighborhood is only needed because in the 1 px resolution testcases,
                        #     the notes drawings are not 4-connected!
                        #     This makes the notes connected components less "clean", but whatever...
                        #     Another solution would be to thicken the drawing (double or triple the resolution
                        #     while forcing overlapping).
                    for vx,vy in V:
                        if 0<=vx<H and 0<=vy<W and P[vx][vy] and (vx,vy) not in note and (vx,vy) not in noted:
                            note.add((vx,vy))
                            noted.add((vx,vy))
                            Q.append((vx,vy))
                Notes.append(note)
    O = []  # output
    for note in Notes:
        # is the tail up or down?
        Imin, Imax = min(i for i,_ in note), max(i for i,_ in note)
        up = sum(int(Imax-i < i-Imin) for i,_ in note)  # pixels closer to the bottom
        is_up = 2*up >= len(note)
        # we derive a line going through the middle of the circle of the note
        Iref = Imax-(DLine+1)//2 if is_up else Imin+DLine//2
        # we check a point around the middle of the circle for the color
        is_black = P[Iref][(min(j for _,j in note)+max(j for _,j in note))//2]
        # nb of half lines from the top line (which is a F)
        Lvl = round((Iref-Line0-1)/(DLine//2))
        # deriving the result
        O.append(chr((5-Lvl)%7 + ord('A')) + ('Q' if is_black else 'H'))
    return O

# image output for the fun
from PIL import Image
def draw_image():
    Img = Image.new('RGB',(W,H),(255,255,255))
    Pix = Img.load()
    for i in range(H):
        for j in range(W):
            if P[i][j]:
                Pix[j,i] = (0,0,0)
                #if on_a_line(i):
                #    Pix[j,i] = (255,0,0)
    #for note in Notes:
    #    for i,j in note:
    #        Pix[j,i] = (255,0,0)
    Img.save('score.png')

def main():
    decode_image()
    identify_lines()
    print(*identify_notes())
    #draw_image()

main()
