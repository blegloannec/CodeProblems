--[[ DISCLAIMER
   Ok so this one is in Lua, because "why not?" and because it seems
   appropriate to solve this "Chip Defects" problem on an "actual" chip!
   The following code ran in 0.7s on a ESP8266 chip with a NodeMCU firmware!
]]

--[[ First of all, a useless recursive formula
   P(k,n) = nb choices leading to <= 2 defects on each chip
   (the proba we look for is 1 - P(k,n) / n^k)
   P(k,n) = P(k,n-1) + k*P(k-1,n-1) + binom(k,2)*P(k-2,n-1)
            0 defect + 1 defect     + 2 defects on chip n
   this would lead to a O(n*k) DP, not good enough!
]]

--[[ A better solution
   For each decomposition k = 2a + b, we choose:
    - a chips (among n) to receive 2 defects
    - 2a defects (among k) for these chips
    - the distribution of these 2a defects on the chips ((2a)! / 2^a)
    - b chips (among n-a remaining) to receive 1 defect
    - the distribution of these b defects on the chips (b!)
   leading to the sum for a=0..k/2 of
   binom(n,a)*binom(k,2a)*fact(2a)/(2^a) * binom(n-a,b)*fact(b)
   Simplifying (remember b = k-2a) and dividing by n^k to directly
   manipulate the proba, we obtain:
   t(a) = 1/n^k * 1/(2^a * a!) * n!/(n-(k-a))! * k!/(k-2a)!
   or again:
   t(0) = 1/n^k * n!/(n-k)! = prod( (n-i)/n, i=1..k-1 )
   t(a+1) = 1/(2*(a+1)) * 1/(n-(k-(a+1))) * (k-2a-1)*(k-2a) * t(a)
   which is finally cheap enough to compute!
]]

function p(k,n)
   local t = 1
   for i = 1,k-1 do t = t * (n-i)/n end
   local p = t
   for a = 0,k/2-1 do
      t = (t*(k-2*a-1)*(k-2*a))/(2*(a+1)*(n-(k-(a+1))))
      p = p + t
   end
   return 1 - p
end

print(p(20000,1000000))
