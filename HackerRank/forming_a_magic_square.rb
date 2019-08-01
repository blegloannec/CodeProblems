#!/usr/bin/env ruby

N = 3
N2 = N*N
S = N*(N2+1)/2

# fast hardcoded size-3 version
def magic3(a)
  a[0]+a[4]+a[8]==S && a[2]+a[4]+a[6]==S &&
    a[0]+a[1]+a[2]==S && a[3]+a[4]+a[5]==S && a[6]+a[7]+a[8]==S &&
    a[0]+a[3]+a[6]==S && a[1]+a[4]+a[7]==S && a[2]+a[5]+a[8]==S
end

# generic version
def magic(a)
  (0...N2).step(N+1).reduce(0){|s,i| s+a[i]}==S &&
    (N-1...N2-1).step(N-1).reduce(0){|s,i| s+a[i]}==S &&
    a.each_slice(N).all?{|r| r.sum==S} &&
    N.times.all?{|i| (i...N2).step(N).reduce(0){|s,i| s+a[i]}==S}
end

def score(a,b)
  a.zip(b).map{|x,y| (x-y).abs}.sum
end

squares = (1..N2).to_a.permutation.select{|a| magic3(a)}
b = N.times.map{gets.split.map(&:to_i)}.flatten
puts squares.map{|a| score(a,b)}.min
