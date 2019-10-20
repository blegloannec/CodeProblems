#!/usr/bin/env ruby

def digits_below(n)
  res = 0
  p10 = 1
  while n>=p10
    res += n - p10 + 1
    p10 *= 10
  end
  res
end

gets.to_i.times do
  l,r = gets.split.map(&:to_i)
  d = digits_below(l-1) + digits_below(r)
  # first index / db(i)-db(l-1) > db(r)-db(i)
  puts (l..r).bsearch {|i| 2*digits_below(i) > d} - 1
end
