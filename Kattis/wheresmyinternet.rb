#!/usr/bin/env ruby

def find(t, u)
  return u if t[u].nil?
  t[u] = find(t, t[u])
  return t[u]
end

def union(t, u, v)
  u = find(t, u); v = find(t, v)
  t[v] = u if u != v
end

def main()
  n,m = gets.split.map &:to_i
  t = [nil]*(n+1)
  m.times {u,v = gets.split.map &:to_i; union(t, u, v)}
  out = (2..n).each.select {|u| find(t, u)!=find(t, 1)}
  puts out.empty? ? 'Connected' : out
end

main()
