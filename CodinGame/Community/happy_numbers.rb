#!/usr/bin/env ruby

# "Be aware that some input numbers are really BIG. Find a way to overcome it."
# Big ints (not a problem in ruby btw) are only a spectre here anyway as
# the largest successor actually is succ(999... 26 times) = 26*9^2 = 2106

def succ(x)
    x.each_char.reduce(0) {|s,c| s + c.to_i**2}.to_s
end

def floyd(s)
    t, h = s, yield(s)
    while t!=h do
        t, h = yield(t), yield(yield(h))
    end
    t
end

n = gets.to_i
n.times do
    s = gets.chomp
    t = floyd(s) {|x| succ(x)}
    puts "#{s} :#{t=='1'?')':'('}"
end
