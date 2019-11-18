#!/usr/bin/env ruby

require 'prime'

n,b = gets.split.map &:to_i
m = n*(n+1)/2
p = m
p += 1 until Prime.prime? p
line = Array.new(n) {|i| i+1 + (i>=n-(p-m) ? 1 : 0)}
if line[-1]<=b then n.times {puts line.join ' '; line.rotate!}
else puts 'impossible' end
