#!/usr/bin/env ruby

S = 10

def components(grid)
    inside = ->(x) {0<=x && x<S}
    black = ->(x,y) {inside.(x) && inside.(y) && grid[x][y]!='.'}
    comp = []
    seen = S.times.map{[false]*S}
    S.times do |i|
        S.times.select{|j| black.(i,j)}.each do |j|
            if !seen[i][j]
                ship = [[i,j]]
                seen[i][j] = true
                s = 0
                while s<ship.size do
                    x0,y0 = ship[s]
                    (x0-1..x0+1).each do |x|
                        (y0-1..y0+1).each.select{|y| black.(x,y)}.each do |y|
                            if !seen[x][y]
                                ship.push([x,y])
                                seen[x][y] = true
                            end
                        end
                    end
                    s += 1
                end
                comp.push(ship)
            end
        end
    end
    comp
end

def valid(grid, comp)
    avail = [0,0,1,2,1,1]
    comp.each do |ship|
        if ship.size<avail.size && avail[ship.size]>0 &&
            (ship.all?{|s| s[0]==ship[0][0]} || ship.all?{|s| s[1]==ship[0][1]})
            avail[ship.size] -= 1
        else
            return false
        end
    end
    avail.all?{|x| x==0}
end

def main()
    shot = gets.chomp
    grid = 10.times.map{gets.chomp}
    sx = shot[1].to_i - 1
    sy = shot[0].ord - 'A'.ord
    coule = ->(ship) {ship.all?{|x,y| grid[x][y]=='_'}}
    comp = components(grid)
    o = []
    if !valid(grid, comp) then o.push("INVALID")
    elsif grid[sx][sy]=='.' then o.push("MISSED")
    else
        grid[sx][sy] = '_'
        touche = comp.find{|ship| ship.include?([sx,sy])}
        o = ["TOUCHE"]
        if coule.(touche)
            o.push(" COULE #{touche.size}")
            if comp.all?{|ship| coule.(ship)} then o.push(" THEN LOSE") end
        end
    end
    puts o.join
end

main()
