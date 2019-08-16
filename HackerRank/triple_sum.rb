#!/usr/bin/env ruby

sizA,sizB,sizC = gets.split.map(&:to_i)
arrA = gets.split.map(&:to_i).sort.uniq
arrB = gets.split.map(&:to_i).sort.uniq
arrC = gets.split.map(&:to_i).sort.uniq
ip = ir = triples = 0
arrB.each do |q|
  ip += 1 while ip<arrA.size && arrA[ip]<=q
  ir += 1 while ir<arrC.size && arrC[ir]<=q
  triples += ip*ir
end
puts triples
