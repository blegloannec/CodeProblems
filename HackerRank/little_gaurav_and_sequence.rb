#!/usr/bin/env ruby

# of course mod 10 there are easy patterns for both sums (see editorial),
# yet the following more generic O(log n) solution is good enough

T = gets.to_i
T.times do
  n = gets.to_i
  s = 0
  p2 = 1
  while p2<=n
    s = (s + 2.pow(p2,10)) % 10
    p2 *= 2
  end
  # sum( 2^(2j), j=0..n ) = (4^(n+1)-1) / (4-1)
  # 4-1 = 3 and 3^(-1) = 7 mod 10
  s = (s * (4.pow(n+1,10)-1)*7) % 10
  puts s
end
