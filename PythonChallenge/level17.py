#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2, StringIO, cookielib, re, bz2, urllib, xmlrpclib

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'

cj = cookielib.CookieJar()
httpcook = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(httpcook)
urllib2.install_opener(opener)
urllib2.urlopen(url)
print iter(cj).next().value

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=%d'
busy = 12345
recipe = []
while False: #True:
    source = urllib2.urlopen(url % busy).read()
    print source
    recipe.append(iter(cj).next().value)
    mo = re.search('[0-9]+$',source)
    if mo==None:
        break
    busy = int(mo.group())

res = ''.join(recipe)
res = 'BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90'

print res
print bz2.decompress(urllib.unquote_plus(res))


rpc = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print rpc.phone('Leopold')


print urllib2.urlopen(urllib2.Request('http://www.pythonchallenge.com/pc/stuff/violin.php',headers={'Cookie':'info='+urllib.quote_plus('the flowers are on their way')})).read()
