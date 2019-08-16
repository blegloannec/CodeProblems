#!/usr/bin/env ruby

# ruby is really amazing at binary search!

N,G = gets.split.map(&:to_i)
Prod = gets.split.map(&:to_i)
puts (0..1<<60).bsearch {|t| Prod.reduce(0){|s,p| s+t/p} >= G}
