#!/usr/bin/env ruby

cas = 1
$<.each_line.each_slice(3) do |ab,cd,_|
  a,b = ab.split.map(&:to_i)
  c,d = cd.split.map(&:to_i)
  det = a*d-c*b
  a,b,c,d = d/det, -b/det, -c/det, a/det
  puts "Case #{cas}:\n#{a} #{b}\n#{c} #{d}"
  cas += 1
end
