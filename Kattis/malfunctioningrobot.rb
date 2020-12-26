#!/usr/bin/env ruby

gets.to_i.times do
  x1,y1,x2,y2 = gets.split.map &:to_i
  a,b = [x2-x1, y2-y1].map(&:abs).sort
  b -= a
  puts  2*a + b + 2*(b/2)
end
