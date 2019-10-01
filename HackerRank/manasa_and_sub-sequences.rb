#!/usr/bin/env ruby

P = 10**9+7

n = gets.chomp.each_char.map(&:to_i)
s = 0  # sum of sub-seqs
c = 1  # count of sub-seqs
n.each do |d|
  s = (s + 10*s + c*d) % P
  c = (2*c) % P
end
puts s
