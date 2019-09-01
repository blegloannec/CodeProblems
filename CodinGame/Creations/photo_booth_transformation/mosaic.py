#!/usr/bin/env python3

from brouillage import Morphimage, Transformaccel, photomaton
from PIL import Image, ImageFont, ImageDraw

font_ttf = '/usr/share/fonts/truetype/ttf-bitstream-vera/VeraMoBd.ttf'

def array_size(L):
    l = 1
    while l*l<=L:
        if L%l==0:
            lines = l
        l += 1
    return L//lines, lines

def mosaic(imgfile, time_list, font_color='white', font_size=11):
    Img = Morphimage(imgfile)
    img0 = Img.Image.copy()
    W,H = img0.size
    L = len(time_list)
    cols,lines = array_size(L)
    Out = Image.new(img0.mode, (W*cols,H*lines))
    T = Transformaccel(photomaton, (W,H))
    Font = ImageFont.truetype(font_ttf, font_size)
    Draw = ImageDraw.Draw(Out)
    for i in range(L):
        t = time_list[i]
        Img.transform(T.iteration(t))
        py,px = divmod(i,cols)
        Out.paste(Img.Image, (W*px,H*py))
        Draw.text((W*px+2,H*py), str(t), font=Font, fill=font_color)
        Img.Image = img0.copy()  # reset
    Out.save('mosaic_'+imgfile)

if __name__=='__main__':
    #mosaic('cri.png', (0,1,2,3,4,103,132,156,572,1009,1715,1716))
    #mosaic('spider.png', (0,1,2,3,4,12,53,82,410,1228,1229,1230))
    mosaic('mondrian.png', (0,1,2,3,4,6,16,17,18), 'teal', 14)
