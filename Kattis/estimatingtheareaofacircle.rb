#!/usr/bin/env ruby

loop do
  r,m,c = gets.split.map(&:to_f)
  break if r==0
  a = Math::PI * r**2
  e = (2*r)**2 * c/m
  puts "#{a} #{e}"
end
