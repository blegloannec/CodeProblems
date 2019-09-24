#!/usr/bin/env ruby

# 11..10****  --snap-->  00..01|****       (bin. incr. on N bits)
#                              |unchanged

T = gets.to_i
T.times do |t|
  n,k = gets.split.map(&:to_i)
  p = 1<<n
  on = (k%p == p-1)
  puts "Case ##{t+1}: #{on ? 'ON' : 'OFF'}"
end
