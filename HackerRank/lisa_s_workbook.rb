#!/usr/bin/env ruby

n,k = gets.split.map(&:to_i)
arr = gets.split.map(&:to_i)
page = 1
res = 0
arr.each do |ex|
  (1..ex).step(k) do |l|
    r = [l+k-1,ex].min
    if l<=page && page<=r then res += 1 end
    page += 1
  end
end
puts res
