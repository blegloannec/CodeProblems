#!/usr/bin/env ruby

def bfs(grid, x0,y0, x1,y1)
  n = grid.size
  dist = n.times.map{[nil]*n}
  dist[x0][y0] = 0
  q = [[x0,y0]]
  while !q.empty?
    x,y = q.shift
    break if x==x1 && y==y1
    [[-1,0],[1,0],[0,-1],[0,1]].each do |dx,dy|
      vx, vy = x+dx, y+dy
      while 0<=vx && vx<n && 0<=vy && vy<n && grid[vx][vy]=='.'
        if dist[vx][vy]==nil  # /!\ not in the loop condition!
          dist[vx][vy] = dist[x][y] + 1
          q.push [vx,vy]
        end
        vx += dx; vy += dy
      end
    end
  end
  dist[x1][y1]
end

N = gets.to_i
G = N.times.map{gets.chomp}
X0,Y0,X1,Y1 = gets.split.map(&:to_i)
puts bfs(G,X0,Y0,X1,Y1)
