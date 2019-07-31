#!/usr/bin/env ruby

require 'set'

def gen(n)
    s = SortedSet.new([1])
    n.times do
        x = s.first
        s.delete(x)
        yield x
        [2,3,5].each{|d| s<<d*x}  # << is .add
    end
end

v = gets.to_i
s = 0
gen(v) {|x| s+=x}
puts s
