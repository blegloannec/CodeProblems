#!/usr/bin/env ruby

# N() = neighborhood, C() = complementary
# 0 initial conf. I
# 1 I
# 2 full O
# 3 C.N(I)
# 4 full O
# 5 C.N(3) = C.N.C.N(I)
# 6 full O
# 7 C.N(5) = C.N.C.N.C.N(I) = C.N(I) = (3)
#   (without proof, N.C.N.C.N(X) = N(X),
#    or alternatively C.N.C.N(Y) = Y for
#    Y = {y such that N(y) is included in N(X)},
#    in particular X is included in Y)
# it loops...

require 'set'

def cn(s)
  res = Set.new((0...$h).to_a.product((0...$w).to_a))
  s.each{|i,j| [[i-1,j],[i+1,j],[i,j],[i,j-1],[i,j+1]].each{|x,y| res.delete([x,y])}}
  res
end

def main()
  $h,$w,t = gets.split.map(&:to_i)
  grid = $h.times.map{gets.chomp}
  if t==1
    out = grid
  elsif t%2==0
    out = $h.times.map{'O'*$w}
  else
    s = Set.new()
    $h.times{|i| $w.times{|j| s.add([i,j]) if grid[i][j]=='O'}}
    s = cn(t%4==3 ? s : cn(s))
    out = $h.times.map{|i| $w.times.map{|j| s.include?([i,j]) ? 'O' : '.'}.join}
  end
  puts out.join("\n")
end

main()
