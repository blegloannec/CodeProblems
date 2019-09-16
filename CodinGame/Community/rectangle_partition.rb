#!/usr/bin/env ruby

w, h, x_cnt, y_cnt = gets.split.map(&:to_i)
ax = [0] + gets.split.map(&:to_i) + [w]
ay = [0] + gets.split.map(&:to_i) + [h]
dx = Hash.new(default=0)
ax.size.times {|i| (i+1...ax.size).each {|j| dx[ax[j]-ax[i]] += 1}}
dy = Hash.new(default=0)
ay.size.times {|i| (i+1...ay.size).each {|j| dy[ay[j]-ay[i]] += 1}}
puts dx.reduce(0) {|a,(d,c)| a+c*dy[d]}
