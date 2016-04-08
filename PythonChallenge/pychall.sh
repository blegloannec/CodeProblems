#!/bin/bash

site="http://www.pythonchallenge.com/pc/def/"
site2="http://www.pythonchallenge.com/pc/return/"
site3="http://www.pythonchallenge.com/pc/hex/"
site4="http://www.pythonchallenge.com/pc/ring/"
site5="http://www.pythonchallenge.com/pc/rock/"

case $1 in
    0)  page="0.html"
	echo "$site$page"
	echo "2^38" | bc;;
    1)  page="$site""map.html"
	echo "$page"
	wget -q -O - "$page" | head -16 | tail -1 | tr abcdefghijklmnopqrstuvwxyz cdefghijklmnopqrstuvwxyzab
	echo "map" | tr abcdefghijklmnopqrstuvwxyz cdefghijklmnopqrstuvwxyzab;;
    2)  page="$site""ocr.html"
	echo "$page"
	wget -q -O - "$page" | tail -n +38 | tr -d '%$_^#@&+(){}[]!*\n';;
    3)  page="$site""equality.html"
	echo "$page"
	wget -q -O - "$page" | grep -o '[^[:upper:]][[:upper:]]\{3\}[[:lower:]][[:upper:]]\{3\}[^[:upper:]]' | cut -c 5 | tr -d "\n";;
    4)  page="$site""linkedlist.php"
	echo "$page"
	page="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
	nothing="12344"
	while true; do
	    source=$(wget -q -O - "$page$nothing")
	    echo $source
	    if [ $nothing -eq 16044 ]; then
		nothing=$(($nothing/2))
	    else
		nothing=$(echo $source | grep -o ' [[:digit:]]*$')
	    fi
	    if [ "$nothing" = "" ]; then
		break
	    fi
	done;;
    5)  page="$site""peak.html"
	echo "$page"
	echo "Level 5 is Python pickle module dependent!"
	./level5.py;;
    6)  page="$site""channel.html"
	echo "$page"
	wget -q "$site""channel.zip"
	rm -rf channel
	unzip -q -d channel channel.zip
	nothing="90052"
	while true; do
	    cat "channel/$nothing.txt"
	    echo
            nothing=$(cat "channel/$nothing.txt" | grep -o ' [[:digit:]]*$' | sed 's/^ //')
	    if [ "$nothing" = "" ]; then
		break
	    fi
	done
	./level6.py
	rm -rf channel channel.zip
	wget -q -O - "$site""hockey.html"
	echo "OXYGEN";;
    7)  page="$site""oxygen.html"
	echo "$page"
	./level7.py;;
    8|9) 
	page="$site""integrity.html"
	page2="$site2""good.html"
	echo "L8 $page"
	echo "L9 $page2"
	./levels8-9.py
	display out.png
	rm -f out.png
	echo "bull";;
    10) page="$site2""bull.html"
	echo "$page (huge/file)"
	suite="1"
	for i in {1..30}; do
	    suite="$(echo -e "$suite" | uniq -c | tr ' ' '\n' | grep '^.')"
	done
	echo "$suite" | wc -l;;
    11) page="$site2""5808.html"
	echo "$page (huge/file)"
	./level11.py
	display out.png
	rm -f out.png;;
    12) page="$site2""evil.html"
	echo "$page (huge/file)"
	./level12.py
	for f in ./out*; do display "$f"; done
	rm -f out*.gif;;
    13) page="$site2""disproportional.html"
	echo "$page"
	./level13.py;;
    14) page="$site2""italy.html"
	echo "$page"
	./level14.py
	display out.png
	rm -f out.png
	echo "cat";;
    15) page="$site2""cat.html"
	echo "$page"
	page="$site2""uzi.html"
	echo "$page"
	./level15.py;;
    16) page="$site2""mozart.html"
	echo "$page"
	./level16.py
	display out.gif
	rm -f out.gif;;
    17) page="$site2""romance.html"
	echo "$page"
	./level17.py;;
    18) page="$site2""balloons.html"
	echo "$page"
	page="$site2""brightness.html"
	echo "$page"
	./level18.py
	for f in out*.png; do display "$f"; done
	rm -f out*.png;;
    19) page="$site3""bin.html (butter/fly)"
	echo "$page"
	./level19.py
	vlc naidni.wav
	rm -f *.wav;;
    20) page="$site3""idiot.html (butter/fly)"
	echo "$page"
	page="$site3""idiot2.html"
	echo "$page"
	./level20.py;;
    21) echo "Level 21 in in the Zip archive from level 20."
	echo "Password: redavni"
	./level21.py;;
    22) page="$site3""copper.html (butter/fly)"
	echo "$page"
	./level22.py
	display bonus.gif
	rm -f bonus.gif;;
    23) page="$site3""bonus.html (butter/fly)"
	echo "$page"
	rot13() { tr "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"; }
	echo "va gur snpr bs jung?" | rot13
	grep -r -i -I 'va gur' /usr/lib/python2.5/*
	module=$(grep -r -i -I 'va gur' /usr/lib/python2.5/* | cut -d: -f1)
	rot13 < "$module" | grep -i 'in the face'
	echo
	echo 'BTW, sending a "sorry" mail to leopold.moz@pythonchallenge.com, we get back a md5 hash bbb8b499a0eef99b52c7f13f4e78c24b for a broken zip with one error.';;
    24) page="$site3""ambiguity.html (butter/fly)"
	echo "$page"
	./level24.py
	echo
	echo 'BTW, inside the .zip from this level, we find the broken zip from Leopold.';;
    25) page="$site3""lake.html (butter/fly)"
	echo "$page"
	rm -rf waves
	mkdir waves
	for i in {1..25}; do
	    wget --user=butter --password=fly -O "waves/lake$i.wav" "$site3""lake$i.wav"
	done
	./level25.py;;
    26) page="$site3""decent.html (butter/fly)"
	echo "$page"
	echo "see brokenzip.py";;
    27) page="$site3""speedboat.html (butter/fly)"
	echo "$page"
	wget -q --user=butter --password=fly "$site3""zigzag.gif"
	./level27.py | tr ' ' '\n' | sort | uniq
	display out.gif
	rm -f zigzag.gif out.gif
	echo "--> repeat and switch are not python key words...";;
    28) page="$site4""bell.html (repeat/switch)"
	echo "$page"
	wget -q --user=repeat --password=switch "$site4""bell.png"
	./level28.py
	rm -f bell.png;;
    29) page="$site4""guido.html (repeat/switch)"
	echo "$page"
	./level29.py;;
    30) page="$site4""yankeedoodle.html (repeat/switch)"
	echo "$page"
	wget -q --user=repeat --password=switch "$site4""yankeedoodle.csv"
	./level30.py
	display formule.png
	rm -f formule.png yankeedoodle.csv;;
    31) page="$site4""grandpa.html (repeat/switch)"
	echo "$page"
	page="$site5""grandpa.html (kohsamui/thailand)"
	echo "$page"
	wget -q --user=kohsamui --password=thailand "$site5""mandelbrot.gif"
	./level31.py
	rm -f mandel*.gif arecibo.gif;;
    32) # nonograms
	page="$site5""arecibo.html (kohsamui/thailand)"
	echo "$page"
        #for f in arecibo.html etch-a-scetch.css etch-a-scetch.js pencil.js warmup.txt; do
    	    #wget -q --user=kohsamui --password=thailand "$site5""$f"
        #done
	page="$site5""up.html (kohsamui/thailand)"
	echo "$page"
	page="$site5""python.html (kohsamui/thailand)"
	echo "$page";;
    33) page="$site5""beer.html (kohsamui/thailand)"
	echo "$page"
	wget -q --user=kohsamui --password=thailand "$site5""beer2.png"
	./level33.py
	rm -f beer2.png
	page="$site5""gremlins.html (kohsamui/thailand)"
	echo "$page";;
    *)	echo "usage: $0 <level>" >&2
	exit 1
esac
