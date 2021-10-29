#!/usr/bin/env ruby

s,m = gets.split.map &:to_i
maxc = gets.split.map &:to_i
curr = [0]*s
m.times do
  req = gets.split.map(&:to_i).zip(maxc).map{|r,c|(r+c-1)/c}
  puts req.zip(curr).map{|r,c|r-c}.join ' '
  curr = req
end
