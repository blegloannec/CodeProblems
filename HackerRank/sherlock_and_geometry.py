#!/usr/bin/env python3

def circle_segment_intersect(xc,yc,R,x1,y1,x2,y2):
    R2 = R*R
    R21 = (x1-xc)**2+(y1-yc)**2
    R22 = (x2-xc)**2+(y2-yc)**2
    if R21<R2 and R22<R2:   # both ends strictly inside
        return False
    if R21<=R2 or R22<=R2:  # one end inside, one outside
        return True
    # both ends strictly outside
    nx,ny = -(y2-y1),x2-x1  # orthogonal vector to the segment
    n2 = nx*nx+ny*ny
    det1 = (x1-xc)*ny-(y1-yc)*nx
    det2 = (x2-xc)*ny-(y2-yc)*nx
    if det1*det2>=0:  # same sign, same side of the circle
        return False
    # the orthogonal projection of x1 to the normal line going
    # through the center has to be inside the circle
    a2 = ((x1-xc)*nx+(y1-yc)*ny)**2
    return a2<=R2*n2

def svg_draw(fname,xc,yc,R,x1,y1,x2,y2,x3,y3):
    mx = min([xc-R,x1,x2,x3])
    Mx = max([xc+R,x1,x2,x3])
    my = min([yc-R,y1,y2,y3])
    My = max([yc+R,y1,y2,y3])
    OPT = 'fill="none" stroke="black" stroke-width="0.5"'
    f = open(fname,'w')
    f.write('<svg width="%d" height="%d">\n' % (Mx-mx,My-my))
    f.write('<circle cx="%d" cy="%d" r="%d" %s />\n' % (xc-mx,yc-my,R,OPT))
    f.write('<path d="M%d %d L%d %d L%d %d Z" %s />\n' % (x1-mx,y1-my,x2-mx,y2-my,x3-mx,y3-my,OPT))
    f.write('</svg>')
    f.close()

def main():
    T = int(input())
    for t in range(T):
        xc,yc,R = map(int,input().split())
        x1,y1 = map(int,input().split())
        x2,y2 = map(int,input().split())
        x3,y3 = map(int,input().split())
        #svg_draw(('out%d.svg'%t),xc,yc,R,x1,y1,x2,y2,x3,y3)
        intersect = circle_segment_intersect(xc,yc,R,x1,y1,x2,y2) or circle_segment_intersect(xc,yc,R,x1,y1,x3,y3) or circle_segment_intersect(xc,yc,R,x3,y3,x2,y2)
        print('YES' if intersect else 'NO')

main()
