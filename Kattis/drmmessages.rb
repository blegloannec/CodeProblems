#!/usr/bin/env ruby

A = 'A'.ord
c = gets.chomp.chars.map{|a|a.ord-A}
l = c.size/2
k = c.sum
puts c[0,l].zip(c[l,l]).map{|a,b|((a+b+k)%26+A).chr}.join
