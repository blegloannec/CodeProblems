gets.to_i.times{|i|gets;puts "Case ##{i+1}: #{gets.split.map(&:to_i).reduce(0){|a,x|a^x}}"}
