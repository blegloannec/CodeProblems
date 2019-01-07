#!/usr/bin/env python3

import os
from PIL import Image, ImageFont, ImageDraw

fanim = 'day15_ascii_slides'
fmono = '/usr/share/fonts/truetype/ttf-bitstream-vera/VeraMoBd.ttf'
col_dict = {'#':(192,192,192,255), '.':(127,127,127,255), 'G':(255,90,90,255), 'E':(90,90,255,255)}
col_def = (220,220,220,255)

if __name__=='__main__':
    mono = ImageFont.truetype(fmono, 12)
    col = lambda c: col_dict[c] if c in col_dict else col_def
    cw,ch = mono.getsize('#')
    A = open(fanim,'r')
    I = A.readlines()
    A.close()
    W = max(len(L.rstrip()) for L in I)
    H = int(I[0])
    for f in range(1,len(I),H):
        Img = Image.new('RGBA',(W*cw,H*ch),0)
        draw = ImageDraw.Draw(Img)
        for i in range(H):
            #draw.text((0,i*ch), I[f+i], font=mono, fill=col_def)  # line all at once
            for j in range(len(I[f+i])):                           # char by char
                c = I[f+i][j]
                draw.text((j*cw,i*ch), c, font=mono, fill=col(c))
        Img.save('gif15/frame%04d.gif' % f)
    os.system('convert -loop 0 -delay 15 gif15/*.gif anim15.gif')
