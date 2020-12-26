#!/usr/bin/env ruby

N = gets.to_i
M = gets.split.map &:to_i
(M.max-1).downto(0) do |d|
  puts M.each.map{|m| d<m ? ' '*d+'/'+'  '*(m-d-1)+'\\'+' '*d : '  '*m}.join.rstrip
end
