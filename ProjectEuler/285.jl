#!/usr/bin/env julia

# JUST BORING!...
# used Sage for no-brain calculations & integrations

# Sage code:
# # (k-1/2)^2 <= (ka+1)^2 + (kb+1)^2 <= (k+1/2)^2
# # fixons b
# # (k-1/2)^2 - (kb+1)^2 <= (ka+1)^2 <= (k+1/2)^2 -(kb+1)^2
# # (sqrt((k-1/2)^2 - (kb+1)^2) - 1) / k <= a <= (sqrt((k+1/2)^2 -(kb+1)^2) - 1) / k
# k,b = var('k,b')
# F1(k,b) = (sqrt((k+1/2)^2-(k*b+1)^2)-1)/k
# F2(k,b) = (sqrt((k-1/2)^2-(k*b+1)^2)-1)/k
# assume(k>1)
# I1(k,b) = integrate(F1(k,b),b)
# I2(k,b) = integrate(F2(k,b),b)
#
# assume(b>0)
# solve((k-1/2)^2-(k*b+1)^2==1,b)
#
# solve((k+1/2)^2-(k*b+1)^2==1,b)
#
# v1 = integrate((sqrt((1+1/2)^2-(1*b+1)^2)-1)/1,b,0,1/2*(sqrt(4*1^2+4*1-3)-2)/1).numerical_approx()
# (v1 + sum(k * ( I1(k,1/2*(sqrt(4*k^2+4*k-3)-2)/k) - I1(k,0) - (I2(k,1/2*(sqrt(4*k^2-4*k-3)-2)/k) - I2(k,0))) for k in range(2,11))).numerical_approx()

# so yeah, yeah, it should be possible to do something cleaner than the following,
# but do we actually care for such a problem?...
I1(k,b) = 1/8*(4*sqrt(-b^2*k^2 - 2*b*k + k^2 + k - 3/4)*b - 8*b - (4*k^2 + 4*k - 3)*asin(-2*(b*k^2 + k)/sqrt((4*k^2 + 4*k - 3)*k^2 + 4*k^2))/k - 4*asin(-2*(b*k^2 + k)/sqrt((4*k^2 + 4*k - 3)*k^2 + 4*k^2))/k + 4*sqrt(-b^2*k^2 - 2*b*k + k^2 + k - 3/4)/k)/k

I2(k,b) = 1/8*(4*sqrt(-b^2*k^2 - 2*b*k + k^2 - k - 3/4)*b - 8*b - (4*k^2 - 4*k - 3)*asin(-2*(b*k^2 + k)/sqrt((4*k^2 - 4*k - 3)*k^2 + 4*k^2))/k - 4*asin(-2*(b*k^2 + k)/sqrt((4*k^2 - 4*k - 3)*k^2 + 4*k^2))/k + 4*sqrt(-b^2*k^2 - 2*b*k + k^2 - k - 3/4)/k)/k

Int1(k) = I1(k,1/2*(sqrt(4*k^2+4*k-3)-2)/k) - I1(k,0)

Int2(k) = I2(k,1/2*(sqrt(4*k^2-4*k-3)-2)/k) - I2(k,0)

# BigFloat for precision (Float64 fails here), runs in ~20s
E = Int1(BigFloat(1))
for k=2:10^5
  E += k * (Int1(BigFloat(k)) - Int2(BigFloat(k)))
end
println(E)
# correctly rounded answer is then 157055.80999
