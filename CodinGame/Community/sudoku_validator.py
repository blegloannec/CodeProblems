#!/usr/bin/env ruby

g = 9.times.map{gets.split.map &:to_i}
p g.all?{|l|l.uniq.size==9} && g.transpose.all?{|l|l.uniq.size==9} && 3.times.all?{|i|3.times.all?{|j|3.times.flat_map{|x|g[3*i+x][3*j,3]}.uniq.size==9}}
