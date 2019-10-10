#!/usr/bin/env ruby

gets.to_i.times do |t|
  n = gets.to_i
  a = gets.split.map(&:to_i).sort
  b = gets.split.map(&:to_i).sort.reverse
  p = a.zip(b).reduce(0){|s,(x,y)| s+x*y}
  puts "Case ##{t+1}: #{p}"
end
