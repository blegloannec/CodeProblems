#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2, Image, cStringIO, ImageDraw

url = 'http://www.pythonchallenge.com/pc/hex/white.gif'
auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password(realm='pluses and minuses',uri=url,user='butter',passwd='fly')
opener = urllib2.build_opener(auth_handler)

## Page à lire :
## http://www.pythonware.com/library/pil/handbook/format-gif.htm

img = Image.open(cStringIO.StringIO(opener.open(url).read()))
w,h = img.size
dst = Image.new(img.mode,(1000,200))
dstdraw = ImageDraw.Draw(dst)
cx,cy = 0,0
while True:
    pix = img.load()
    ## Le GIF animé contient 133 frames
    ## À chaque frame, il y a exactement 1 pixel non noir
    ## Parmi {98,100,102}^2
    ##for x in range(w):
    ##    for y in range(h):
    ##        if pix[x,y]!=0:
    ##            dpix[x,y]=255
    ##            print x,y
    for x in [98,100,102]:
        for y in [98,100,102]:
            if pix[x,y]!=0:
                ox,oy = cx,cy
                cx += 4*(x-100)
                cy += 4*(y-100)
                if (x,y)==(100,100):
                    cx += 150
                else:
                    dstdraw.line([ox,oy,cx,cy],fill=255)
    try:
        img.seek(img.tell()+1) ## next frame
    except:
        break

dst.save('bonus.gif')
