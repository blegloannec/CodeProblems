#!/usr/bin/env ruby

x,y,x1,y1,x2,y2 = gets.split.map &:to_f
if x<x1
  if    y<y1  then puts Math.hypot(x1-x, y1-y)
  elsif y<=y2 then puts x1-x
  else             puts Math.hypot(x1-x, y-y2)
  end
elsif x<=x2
  if    y<y1  then puts y1-y
  elsif y<=y2 then fail
  else             puts y-y2
  end
else
  if    y<y1  then puts Math.hypot(x-x2, y1-y)
  elsif y<=y2 then puts x-x2
  else             puts Math.hypot(x-x2, y-y2)
  end
end
