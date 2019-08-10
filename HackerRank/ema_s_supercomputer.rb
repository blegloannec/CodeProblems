#!/usr/bin/env ruby

# kinda not-too-inefficient implementation below
# (brute force was good enough to pass and way less tricky though...)

def score(r1,r2)
  (4*(r1-1)+1) * (4*(r2-1)+1)
end

H,W = gets.split.map(&:to_i)
N = H*W
Good = H.times.map{gets.chomp.each_char.map{|c| c=='G'}}
Crosses = N.times.map{|a| a.divmod(W)}.select{|i,j| Good[i][j]}

cross = H.times.map{W.times.map{[]}}
H.times do |i|
  g = 0
  0.upto(W-1)     {|j| g = Good[i][j] ? g+1 : 0; cross[i][j].push(g)}
  g = 0
  (W-1).downto(0) {|j| g = Good[i][j] ? g+1 : 0; cross[i][j].push(g)}
end
W.times do |j|
  g = 0
  0.upto(H-1)     {|i| g = Good[i][j] ? g+1 : 0; cross[i][j].push(g)}
  g = 0
  (H-1).downto(0) {|i| g = Good[i][j] ? g+1 : 0; cross[i][j].push(g)}
end

cross = H.times.map{|i| W.times.map{|j| cross[i][j].min}}
vmax = 0
(0...Crosses.size).each do |a|
  i1,j1 = Crosses[a]
  (a+1...Crosses.size).each do |b|
    i2,j2 = Crosses[b]
    cmin,cmax = [cross[i1][j1],cross[i2][j2]].sort
    dmin,dmax = [(i1-i2).abs,(j1-j2).abs].sort
    if dmin==0  # aligned crosses
      d = dmax+1
      cmin = [cmin,d/2].min
      cmax = [cmax,d-cmin].min
      v = score(cmin,cmax)
    else
      if cmin>dmin && cmax>dmax  # crosses intersect -- tricky case
        v = [score(dmin-1,cmax), score([cmin,dmax].min,dmax)].max
      else
        v = score(cmin,cmax)
      end
    end
    vmax = v if v>vmax
  end
end
puts vmax
