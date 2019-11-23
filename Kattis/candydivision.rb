#!/usr/bin/env ruby

require 'prime'

n = gets.to_i
divs = [1]
Prime.prime_division(n).each do |p,m|
  s = divs.size
  q = p
  m.times do
    s.times {|i| divs.push(divs[i]*q)}
    q *= p
  end
end
divs.sort!
puts divs.map{|d| d-1}.join(' ')
