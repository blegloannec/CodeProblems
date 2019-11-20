#!/usr/bin/env ruby

n = gets.to_i
a = gets.split.map(&:to_i)
o = Array.new(n){|i|i+1}.sort_by{|i|a[i-1]}.reverse
puts 2*a[o[0]-1]<=a.sum ? o.join(' ') : 'impossible'
