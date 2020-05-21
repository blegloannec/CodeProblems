#!/usr/bin/env ruby

require 'prime'

while true
  n = gets.to_i
  break if n==0
  k = Prime.prime_division(n.abs).reduce(0){|g,(_,m)|g.gcd(m)}
  if n<0 then
    k >>= 1 while k&1==0
  end
  p k
end
