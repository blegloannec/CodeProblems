#!/usr/bin/env ruby

D = 'SENW'
f0,t0,f1 = gets.split.map{|d|d[0]}
i = D.index(f0)
puts ['NE','WN','WE'].include?(D[D.index(t0)-i]+D[D.index(f1)-i]) ? 'Yes' : 'No'
