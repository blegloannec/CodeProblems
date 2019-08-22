#!/usr/bin/env ruby

def stacks_game(a, b, x)
  (1...a.size).each {|i| a[i] += a[i-1]}
  (1...b.size).each {|i| b[i] += b[i-1]}
  i = 0; j = b.size-1; cnt = 0
  while i<a.size && a[i]<=x
    j -= 1 while j>0 && a[i]+b[j]>x
    cnt = i+j if i+j>cnt
    i += 1
  end
  cnt
end

g = gets.to_i
g.times do
  n,m,x = gets.split.map(&:to_i)
  a = [0] + gets.split.map(&:to_i)
  b = [0] + gets.split.map(&:to_i)
  puts stacks_game(a,b,x)
end
