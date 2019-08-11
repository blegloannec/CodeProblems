#!/usr/bin/env ruby

# simple DP, same as CG/Community/robbery_optimisation.py

N = gets.to_i
arr = gets.split.map{|x| [0,x.to_i].max}
arr[1] = arr[0..1].max if N>1
(2...N).each {|i| arr[i] = [arr[i-1], arr[i-2]+arr[i]].max}
puts arr[-1]
