#!/usr/bin/env ruby

gets.to_i.times do
  x = gets.chomp
  puts x.size.times.map{|s| x[0..s].to_i.to_s(2).count('1')}.max
end
