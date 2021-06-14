#!/usr/bin/env ruby

a,b = gets.split.map &:to_i
cnt = 0
while a>b
  cnt += 1
  if a&1==0
    a >>= 1
  else
    a += 1
  end
end
cnt += b-a
puts cnt
