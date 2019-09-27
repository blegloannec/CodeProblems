#!/usr/bin/env ruby

def draw_pattern(n)
  tri = [[0,1,0]]
  (n-1).times do
    tri.push [0,1]
    (2...tri[-2].size).each {|j| tri[-1].push(tri[-2][j-2..j].sum%2)}
    tri[-1] += [1,0]
  end
  tri.each {|l| puts l[1..l.size-2].map{|c| c==0 ? '.' : '#'}.join}
  tri.each_with_index {|l,i| puts '%2d %s' % [i,l[1..[4,l.size-2].min].join]}
end

def main
  #draw_pattern(1<<4)
  t = gets.to_i
  t.times do
    n = gets.to_i
    puts n<=2 ? -1 : [3,2,4,2][n%4]
  end
end

main
