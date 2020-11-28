#!/usr/bin/env ruby

loop do
  h,t = gets.split.map &:to_i
  break if h==0
  res = 0
  if t.odd?
    t += 1
    res += 1
  end
  if (h+t/2).odd?
    t += 2
    res += 2
  end
  res += t/2 + (t/2+h)/2
  puts res
end
