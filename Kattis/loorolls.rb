#!/usr/bin/env ruby

l,n = gets.split.map &:to_i  # n<=l
r = 0
while n>0
  r += 1
  n = (-l)%n  # what remains to be taken on the next roll
end
puts r
