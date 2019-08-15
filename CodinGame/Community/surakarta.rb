#!/usr/bin/env ruby
# coding: utf-8

=begin
╭───╮╭───╮
│╭─╮││╭─╮│
││┏┿┿┿┿┓││
│╰╂┼┼O┼╂╯│
╰─╂┼┼┼┼╂─╯
╭─╂X┼┼┼╂─╮
│╭╂┼┼┼┼╂╮│
││┗┿┿┿┿┛││
│╰─╯││╰─╯│
╰───╯╰───╯
=end

G = 6.times.map{gets.chomp}.join
res = 0
['#!()*+,-!&,28>D!?>=<;:!A;5/)','$!./0123!%+17=C!987654!B<60*'].each do |c|
    s = c.chars.flat_map{|c| c=='!' ? [c] : {'.'=>[],'O'=>['O'],'X'=>[c]}[G[c.ord-34]]}
    [s,s.reverse].each{|s| s.size.times{res+=1 if s.uniq[1..2].join=='!O'; s.rotate!}}
end
puts res
