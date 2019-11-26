#!/usr/bin/env ruby

# No difference with usual Nim as adding chips to a 0-xor will necessarily
# make it non 0 and the player who has a winning (non 0-xor) position can
# always keep his add-moves to reverse its opponents adds so that he always
# preserve his winning position.

gets.to_i.times do
  gets
  puts gets.split.map(&:to_i).reduce(0){|x,p|x^p}!=0 ? 'First' : 'Second'
end
