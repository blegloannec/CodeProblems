#!/usr/bin/env ruby

# See also the following for interesting perspectives/applications:
# https://rjlipton.wordpress.com/2014/08/19/the-derivative-of-a-number/

require 'prime'
n = gets.to_i
puts Prime.prime_division(n).map{ |p,m| m*n/p }.sum
