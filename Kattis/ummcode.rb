#!/usr/bin/env ruby

puts gets.split.map{|w|w.gsub(/[\W_]/,'')}.select{|w|w=~/^[mu]+$/}.join.tr('mu','01').chars.each_slice(7).map{|c|c.join.to_i(2).chr}.join
