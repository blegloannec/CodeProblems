#!/usr/bin/env ruby

l,r = gets.split(" ").map(&:to_i)
v = (l..r).map{|x| x**3}
s = v.size-1
w = (0...s).map{|i| (i+1..s).map{|j| v[i]+v[j]}}.flatten.sort.chunk{|x| x}.map{|_,l| l.size}
vol_cnt = w.count{|c| c>1}
fun_cnt = w.map{|c| c*(c-1)}.sum
puts "#{vol_cnt} #{fun_cnt}"
