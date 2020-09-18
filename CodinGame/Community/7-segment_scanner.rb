#!/usr/bin/env ruby

D = ['_| ||','   | ','_ _||','_ _| ',' |_| ','_|_  ','_|_ |','_  | ','_|_||','_|_| ']
a,b,c = 3.times.map{gets.chop}
puts (0...a.size).step(3).map{|i| D.index(a[i+1]+b[i,3]+c[i]).to_s}.join
