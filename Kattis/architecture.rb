#!/usr/bin/env ruby

# Obviously we need max X = max Y.
# Conversely, if Xi = max X = max Y = Yj, then one valid
# solution is to use:
#  - Y as the i-th line
#  - X as the j-th column
#  - 0s everywhere else

r,c = gets.split.map &:to_i
x = gets.split.map &:to_i
y = gets.split.map &:to_i
puts (x.max==y.max ? '' : 'im') + 'possible'
