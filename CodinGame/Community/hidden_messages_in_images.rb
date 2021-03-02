#!/usr/bin/env ruby

w,h = gets.split.map &:to_i
puts [h.times.flat_map{gets.split.map{|x|(x.to_i&1).to_s}}.join].pack 'B*'
