#!/usr/bin/env ruby

prim = [2,3,5,7,11,13,17,19]
prod = Array.new(prim)
(1...prod.size).each {|i| prod[i] *= prod[i-1]}
prod.unshift 1
total = prod.pop
curr = gets.split.map(&:to_i).zip(prod).reduce(0){|s,(x,p)| s += x*p}
puts total-curr-1

# one liner:
# p 9699689-gets.split.map(&:to_i).zip([1,2,6,30,210,2310,30030,510510]).map{|x,p|x*p}.sum
