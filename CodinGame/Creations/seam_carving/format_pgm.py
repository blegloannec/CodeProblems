#!/usr/bin/env python3

import sys, os, argparse
from PIL import Image

MAXSIZE = 10000

def pgm_str(Img, shrink=0):
    assert shrink<Img.width
    Pix = Img.load()
    O = ['P2', '%d %d'%Img.size]
    if shrink>0:
        O.append('# %d' % (Img.width-shrink))
    O.append('255')
    for i in range(Img.height):
        O.append(' '.join(str(Pix[j,i]) for j in range(Img.width)))
    O.append('')
    return '\n'.join(O)

def resize(Img, a):
    asize = (round(a*Img.width), round(a*Img.height))
    return Img.resize(asize, Image.ANTIALIAS)

if __name__=='__main__':
    Parser = argparse.ArgumentParser()
    Parser.add_argument('img_file', nargs='+')
    Parser.add_argument('--maxsize', type=int, default=10000)
    Parser.add_argument('--shrink', type=int, default=0)
    Parser.add_argument('--out')
    Args = Parser.parse_args()
    for file_name in Args.img_file:
        Img = Image.open(file_name).convert('L')
        l,r = 0.,1.
        while r-l>0.001:
            a = (l+r)/2.
            L = len(pgm_str(resize(Img,a), Args.shrink))
            if L>Args.maxsize:
                r = a
            else:
                l = a
        if Args.out is None:
            out_name = os.path.splitext(os.path.basename(file_name))[0] + '.pgm'
        else:
            out_name = Args.out
        F = open(out_name, 'w')
        F.write(pgm_str(resize(Img,l), Args.shrink))
        F.close()
