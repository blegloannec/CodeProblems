#!/usr/bin/env ruby

N = n = gets.to_i + 1
cnt1 = 0
p2 = 1
while n!=0
    q,r = N.divmod p2
    cnt1 += (q/2)*p2 + (q%2)*r
    p2 <<= 1
    n >>= 1
end
puts cnt1
