#!/usr/bin/env python

#from PIL import Image

# It's obviously the equation of a black disc.
# Each node of the tree is responsible for a square
# and this square is completely black/white iff
# the four vertices are of the same color, except
# for the root (the previous condition is valid once
# we are in a quarter circle).

N = 24
S = 1<<N
CX = CY = 1<<(N-1)
R2 = 1<<(2*N-2)
def black(x,y):
    return (x-CX)**2 + (y-CY)**2 <= R2

# generating the image, for the sake of fun!
# used N = 10
def gen_img():
    img = Image.new('1',(S,S),1)
    pix = img.load()
    for x in xrange(S):
        for y in xrange(S):
            if black(x,y):
                pix[x,S-1-y] = 0
    img.save('out.png')

#gen_img()

# counting nodes of the quadtree
def count_nodes(root=True,x1=0,y1=0,x2=S-1,y2=S-1):
    if not root and black(x1,y1)==black(x1,y2)==black(x2,y1)==black(x2,y2):
        return 2 # 10 or 11
    # otherwise there is a split 0 + 4 children
    cx,cy = (x1+x2)/2,(y1+y2)/2
    return 1+count_nodes(False,x1,y1,cx,cy)+count_nodes(False,x1,cy+1,cx,y2)+count_nodes(False,cx+1,y1,x2,cy)+count_nodes(False,cx+1,cy+1,x2,y2)

print count_nodes()
