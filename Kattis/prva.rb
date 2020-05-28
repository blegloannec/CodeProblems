#!/usr/bin/env ruby

h,w = gets.split.map &:to_i
g = h.times.map{gets.chomp.chars}
puts (g+g.transpose).flat_map{|l|l.join.split'#'}.select{|w|w.size>1}.min
