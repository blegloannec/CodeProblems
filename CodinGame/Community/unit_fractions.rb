#!/usr/bin/env ruby

# x >= y > n > 0
# 1/n = 1/x + 1/y <=> n^2 = (x-n)(y-n)
# see also PE 108 & 110

n = gets.to_i
n2 = n*n
(1..n).each {|x| puts "1/#{n} = 1/#{n2/x+n} + 1/#{x+n}" if n2%x==0}
