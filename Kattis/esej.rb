#!/usr/bin/env ruby

puts gets.split[1].to_i.times.map{'abcdefghi'.chars.shuffle.join}.join ' '
