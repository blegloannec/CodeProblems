#!/usr/bin/env ruby

s = gets.rstrip.chars
t = gets.rstrip.chars
k = gets.to_i
p = s.zip(t).take_while {|a,b| a==b}.size
tot = s.size + t.size
opt = tot - 2*p
res = k>=tot || (opt<=k && (k-opt)%2==0)
puts res ? 'Yes' : 'No'
