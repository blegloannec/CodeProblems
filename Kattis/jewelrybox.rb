#!/usr/bin/env ruby
# coding: utf-8

gets.to_i.times do
  x,y = gets.split.map &:to_f
  # a = x-2h, b = y-2h
  # maximize f(h) = abh = 4h³ - 2(x+y)h² + xyh
  #  => f'(h) = 12h² - 4(x+y)h + xy = 0
  d = Math.sqrt(x*x+y*y-x*y)
  h = (x+y-d)/6.0
  puts (x-2.0*h)*(y-2.0*h)*h
end
