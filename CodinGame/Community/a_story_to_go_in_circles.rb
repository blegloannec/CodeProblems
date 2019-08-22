#!/usr/bin/env ruby

T = gets.to_i-1
S = gets.to_i
grids = [ S.times.map {gets.chomp.chars} ]
3.times { grids.push grids.last.transpose.map {|l| l.reverse} }

g = x = y = t = 0
hist = []; time = {}
while t<T
    pos = [g,x,y]
    if time.has_key? pos
        t0 = time[pos]
        g,x,y = hist[(T-t0)%(t-t0) + t0]
        break
    end
    if    grids[g][x][y]=='#' then g = (g+1)%4
    elsif grids[g][x][y]=='@' then g = (g-1)%4
    else
        time[pos] = t; hist.push pos
        m = grids[g][x][y].ord - 'a'.ord + 1
        dx,y = (y+m).divmod(S)
        x = (x+dx)%S
        t += 1
    end
end
puts grids[g][x][y]
