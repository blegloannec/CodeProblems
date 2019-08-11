#!/usr/bin/env ruby

# O(N * A.max) maintaining a frequency array of the running window
# NB: This was the expected approach here as A.max is small,
#     although this can also be solved in O(N log N) using 2 heaps
#     (a max-heap for the lower half of the window and
#      a min-heap for the upper half).
#     see HR/find_the_running_median.py for that approach

# returns the double of the median given the frequency array
def median2(cnt, d)
  c = 0
  left_med = nil
  (0...cnt.size).each do |i|
    c += cnt[i]
    left_med = i if left_med==nil && 2*c>=d
    return left_med+i if 2*c>d
  end
end

N,D = gets.split.map(&:to_i)
A = gets.split.map(&:to_i)
cnt = [0]*(A.max+1)
(0...D).each {|i| cnt[A[i]] += 1}
notif = 0
(D...N).each do |i|
  notif += 1 if A[i] >= median2(cnt, D)
  cnt[A[i-D]] -= 1
  cnt[A[i]]   += 1
end
puts notif
