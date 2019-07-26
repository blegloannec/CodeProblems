#!/usr/bin/env ruby

require 'set'

def gen(n)
    s = SortedSet.new([1])
    seen = Set.new([1])
    n.times do
        x = s.first
        s.delete(x)
        yield x
        # === is .include?  and  << is .add
        [2,3,5].map{|d| d*x}.select{|y| !(seen===y)}.each{|y| seen<<y; s<<y}
    end
end

v = gets.to_i
s = 0
gen(v) {|x| s+=x}
puts s
