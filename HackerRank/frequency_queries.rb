#!/usr/bin/env ruby

class Custom
  def initialize
    @elem_cnt = Hash.new(default=0)
    @cnt_freq = Hash.new(default=0)
  end

  def insert(x)
    if @elem_cnt[x]>0 then @cnt_freq[@elem_cnt[x]] -= 1 end
    @elem_cnt[x] += 1
    @cnt_freq[@elem_cnt[x]] += 1
  end

  def delete(x)
    if @elem_cnt[x]>0
      @cnt_freq[@elem_cnt[x]] -= 1
      @elem_cnt[x] -= 1
      @cnt_freq[@elem_cnt[x]] += 1
    end
  end

  def check(f)
    @cnt_freq[f] > 0
  end
end

struct = Custom.new
gets.to_i.times do
  t,x = gets.split.map(&:to_i)
  if t==1 then struct.insert(x)
  elsif t==2 then struct.delete(x)
  else puts struct.check(x) ? '1' : '0' end
end
