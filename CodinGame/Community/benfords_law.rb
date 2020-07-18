#!/usr/bin/env ruby

P = [nil, 30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
n = gets.to_i
c = n.times.map{gets[/[1-9]/].to_i}
p (1..9).any?{|d| (100.0*c.count(d)/n-P[d]).abs > 10.0}
