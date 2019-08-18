#!/usr/bin/env ruby

N = 10**6+1
dp = N.times.map{|i| i}
(1...N).each do |i|
  dp[i] = dp[i-1]+1 if dp[i-1]+1<dp[i]
  k = 2
  while k<=i && k*i<N
    dp[k*i] = dp[i]+1 if dp[i]+1<dp[k*i]
    k += 1
  end
end

gets.to_i.times {puts dp[gets.to_i]}
