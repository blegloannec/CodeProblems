#!/usr/bin/env ruby

n,r = gets.split.map(&:to_i)
arr = gets.split.map(&:to_i)
freq_single = Hash.new(default=0)
freq_couple = Hash.new(default=0)
triples = 0
arr.reverse.each do |x|
  triples += freq_couple[r*x]
  freq_couple[x] += freq_single[r*x]
  freq_single[x] += 1
end
puts triples
