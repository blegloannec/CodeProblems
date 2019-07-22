#!/usr/bin/env ruby

n = gets.to_i
a = gets.split(" ").map(&:to_i).sort.chunk{|x| x}.map{|x,l| [x,l.size]}
res = 0
until a.empty? do
    x,l = a.shift
    if l>1
        if !a.empty? && a[0][0]==x+1
            a[0][1] += l/2
        else
            a.unshift([x+1,l/2])
        end
    end
    res += l%2
end
puts res
