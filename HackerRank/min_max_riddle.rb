#!/usr/bin/env ruby

n = gets.to_i
a = gets.split.map(&:to_i)
a.push(-1)  # push -1 => a will be fully popped at the end
w = [-1]*(n+1)  # results

# stack-based previous lower (& greater by the trick) element
s = [-1]  # sentinel for convenience
a.size.times do |i|
  while s.size>1 && a[s.last]>=a[i]
    # for m = a[-1] and l = a[-2], the moment i we pop m, we have:
    #  - a[l] is the previous lower element of a[m]
    #  - a[i] is the next greater element of a[m]
    #  - a[m] is the min of all intervals [u,v] with l < u <= m <= v < i
    # the greatest such interval is [l+1,i-1] of size d = i-l-1
    # then all intervals of size <= d must have w[d] >= a
    x = a[s.pop]
    d = i - s.last - 1
    w[d] = x if x>w[d]
  end
  s.push(i)
end

# final propagation
(n-1).downto(1) {|i| w[i] = w[i+1] if w[i+1]>w[i]}

puts w[1..n].join(' ')
