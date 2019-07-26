#!/usr/bin/env lua5.3

-- Heaps
function heap_push(H,x)
    table.insert(H,x)
    local i, j = #H, #H//2
    while i>1 and H[j]>H[i] do
        H[i], H[j] = H[j], H[i]
        i, j = j, j//2
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
        l, r = 2*i, 2*i+1
    end
    return top
end
--

N = tonumber(io.read())
next_token = string.gmatch(io.read(), "[^%s]+")
H = {}
for i=1,N do
    heap_push(H, tonumber(next_token()))
end
res = 0
while #H>1 do
    local x = heap_pop(H) + heap_pop(H)
    res = res + x
    heap_push(H,x)
end
print(res)
