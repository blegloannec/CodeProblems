#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2

url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'
auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password(realm='pluses and minuses',uri=url,user='butter',passwd='fly')
opener = urllib2.build_opener(auth_handler)

print opener.open(url).info()

# On balaye le début des données cachées,
# seul le début des ranges semble compter pour le serveur.
p = 30203
while True:
    try:
        o = opener.open(urllib2.Request(url,headers={'Range':'bytes=%d-%d'%(p,p+1000)}))
        d = o.read()
        print o.info()
        print d
        p += len(d)
    except:
        break

# On balaye la fin des données cachées,
# seule la fin des ranges semble compter pour le serveur.
p = 2123456789
while True:
    try:
        o = opener.open(urllib2.Request(url,headers={'Range':'bytes=%d-%d'%(p-1,p)}))
        d = o.read()
        print o.info()
        print d
        p -= len(d)
    except:
        break

print 'esrever ni emankcin wen ruoy si drowssap eht'[::-1]
print '--> redavni'

p = 1152983631
o = opener.open(urllib2.Request(url,headers={'Range':'bytes=%d-%d'%(1152983631,p+1)}))
print o.info()
f = open('level21.zip','w')
f.write(o.read())
f.close()
