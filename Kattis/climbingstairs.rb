#!/usr/bin/env ruby

n,r,k = gets.split.map &:to_i
d = k+(r-k).abs
puts d>=n ? d+r : n+r+(n-r)%2
