#!/usr/bin/env ruby

# https://en.wikipedia.org/wiki/Dolbear%27s_law

def avg(n, meas)
  cnt = meas.size/n
  meas.each_slice(n).take(cnt).map{|b| yield b.sum}.sum / cnt
end

def dolbear(meas)
  [avg(15, meas) {|n| 10.0 + (n-40.0)/7.0},
   avg( 2, meas) {|n| n + 5.0}]
end

M = gets.to_i
Meas = M.times.flat_map{gets.split.map(&:to_i)}
t1,t2 = dolbear(Meas).map{|t| t.round(1)}
puts t1
puts t2 if 5.0<=t1 && t1<=30.0
