#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2, base64, wave, array

url = 'http://www.pythonchallenge.com/pc/hex/bin.html'

auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password(realm='pluses and minuses',uri=url,user='butter',passwd='fly')
opener = urllib2.build_opener(auth_handler)
f = open('indian.wav','w')
f.write(base64.standard_b64decode(''.join(opener.open(url).readlines()[27:-4])))
f.close()

print 'inverted India => inverted endian'

src = wave.openfp('indian.wav','rb')
dst = wave.openfp('naidni.wav','wb')
dst.setparams(src.getparams())
## Cette ligne renvoie le bon fichier mais avec le son lu à l'envers !
#dst.writeframes(src.readframes(src.getnframes())[::-1])
## La bonne solution est de renverser chaque octet :
a = array.array('i')
a.fromstring(src.readframes(src.getnframes()))
a.byteswap()
dst.writeframes(a.tostring())
src.close()
dst.close()
