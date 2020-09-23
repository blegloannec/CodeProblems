#!/usr/bin/env ruby

# m = 5, n = 6
# Win? -----++++++-----++++++-----++++++...
#      0    m     m+n  2m+n  2m+2n

k,m,n = gets.split.map &:to_i
puts k%(m+n) < m ? 'Barb' : 'Alex'
