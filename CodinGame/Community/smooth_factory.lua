#!/usr/bin/env lua

-- Heaps
function heap_push(H,x)
   table.insert(H,x)
   local i = #H
   local j = math.floor(i/2)
   while i>1 and H[j]>H[i] do
      H[i], H[j] = H[j], H[i]
      i = j
      j = math.floor(i/2)
   end
end

function heap_pop(H)
   assert(#H>0)
   H[1], H[#H] = H[#H], H[1]
   local top = table.remove(H)
   local i, l, r = 1, 2, 3
   while (l<=#H and H[l]<H[i]) or (r<=#H and H[r]<H[i]) do
      local j = i
      if r<=#H and H[r]<H[l] then
	 i = r
      else
	 i = l
      end
      H[i], H[j] = H[j], H[i]
      l = 2*i
      r = l+1
   end
   return top
end
--


function gen()
   local D = {2,3,5}
   local seen = {[1] = true}
   local H = {1}
   while true do
      local x = heap_pop(H)
      for _,d in ipairs(D) do
	 local y = x*d
	 if seen[y]==nil then
	    seen[y] = true
	    heap_push(H,y)
	 end
      end
      coroutine.yield(x)
   end
end

V = tonumber(io.read())
cogen = coroutine.create(gen)
s = 0
for i=1,V do
   local _,x = coroutine.resume(cogen)
   s = s + x
end
print(string.format("%d",s))
