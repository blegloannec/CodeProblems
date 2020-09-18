#!/usr/bin/env ruby

def find(repr, x)
  return x if repr[x] == nil
  repr[x] = find(repr, repr[x])
  return repr[x]
end

def union(repr, size, x, y)
  x0 = find(repr, x)
  y0 = find(repr, y)
  if x0 != y0
    repr[y0] = x0
    size[x0] += size[y0]
  end
end

def main()
  n = gets.to_i
  m = gets.to_i
  repr = [nil]*n
  size = [1]*n
  m.times do
    u, v = gets.split.map &:to_i
    union(repr, size, u, v)
  end
  out = [0]*(n+1)
  n.times do |u|
    out[size[u]] += 1 if find(repr, u) == u
  end
  n.downto(1) do |s|
    puts "#{s} #{out[s]}" if out[s] > 0
  end
end

main()
