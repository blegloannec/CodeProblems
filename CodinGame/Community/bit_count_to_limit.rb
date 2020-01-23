#!/usr/bin/env ruby

m = gets.to_i
n = m+1
cnt1 = 0
p2 = 1
while m!=0
    q,r     = n.divmod p2
    blk,par = q.divmod 2
    cnt1 += blk*p2 + par*r
    p2 <<= 1
    m  >>= 1
end
puts cnt1
