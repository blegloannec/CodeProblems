#!/usr/bin/env ruby

sides = gets.to_i
bets = sides.times.map {i,mul,mny = gets.split; [i.to_i, mul.to_f, mny.to_f]}
total = bets.reduce(0) {|s,b| s+b[2]}
i,mul,mny = bets.min_by{|i,mul,mny| (mul+1)*mny}
win = total - (mul+1)*mny
puts '%d %.2f' % [i, win.round(2)]
