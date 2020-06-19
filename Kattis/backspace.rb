#!/usr/bin/env ruby

o = []
gets.each_char{|c| c=='<' ? o.pop : o.push(c)}
puts o.join
