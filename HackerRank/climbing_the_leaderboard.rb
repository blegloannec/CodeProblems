#!/usr/bin/env ruby

n = gets.to_i
s = gets.split.map(&:to_i).uniq
m = gets.to_i
a = gets.split.map(&:to_i)

i = s.size-1
a.each do |x|
  while i>=0 && s[i]<=x do i -= 1 end
  puts i+2
end
