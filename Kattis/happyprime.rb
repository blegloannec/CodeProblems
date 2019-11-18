#!/usr/bin/env ruby

require 'prime'

$memo = {1=>true, 4=>false}
def happy(n)
  $memo[n] = happy(n.to_s.each_char.reduce(0){|a,c|a+c.to_i**2}) unless $memo.has_key?(n)
  $memo[n]
end

t = gets.to_i
t.times do
  k,n = gets.split.map(&:to_i)
  hp = Prime.prime?(n) && happy(n)
  puts "#{k} #{n} #{hp ? 'YES' : 'NO'}"
end
