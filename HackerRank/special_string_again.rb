#!/usr/bin/env ruby

n = gets.to_i
s = gets.chomp.each_char.chunk{|x| x}.map{|x,l| [x,l.size]}
aaa = s.map{|x,l| l*(l+1)/2}.sum
aba = s.each_cons(3).map{|l,m,r| m[1]==1 && l[0]==r[0] ? [l[1],r[1]].min : 0}.sum
puts aaa+aba
