#!/usr/bin/env ruby

h,w = gets.split.map &:to_i
g = h.times.map{ gets.chomp }
q = []
push = ->(i,j){ q.push [i,j]; g[i][j] = 'V' }
h.times{|i| w.times{|j| q.push [i,j] if g[i][j]=='V' }}
while !q.empty?
  i,j = q.pop
  if i+1<h
    if g[i+1][j]=='.' then push.(i+1,j)
    elsif g[i+1][j]=='#'
      push.(i,j-1) if j  >0 && g[i][j-1]=='.'
      push.(i,j+1) if j+1<w && g[i][j+1]=='.'
    end
  end
end
g.each{|l| puts l}
