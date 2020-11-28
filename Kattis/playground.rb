#!/usr/bin/env ruby

# reduces to the same question for a polygon by replacing
# each half-circle by its diameter and observing that if
# this is possible, then this can always be done in the plane

loop do
  k = gets.to_i
  break if k==0
  a = gets.split.map(&:to_f).sort
  pos = false
  s = 0
  a.each do |x|
    pos = s>=x
    break if pos
    s += x
  end
  puts pos ? 'YES' : 'NO'
end
