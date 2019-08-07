#!/usr/bin/env ruby

# classic, only to experiment ruby classes...

class Queue
  def initialize
    @in_stk = []
    @out_stk = []
  end

  def push(x)
    @in_stk.push x
  end

  def transfer
    if @out_stk.empty?
      while !@in_stk.empty? do
        @out_stk.push @in_stk.pop
      end
    end
  end

  def front
    transfer
    @out_stk[-1]
  end 

  def pop
    transfer
    @out_stk.pop
  end
end

q = Queue.new
gets.to_i.times do
  t,x = gets.split.map &:to_i
  if t==1 then q.push x
  elsif t==2 then q.pop
  else puts q.front end
end
