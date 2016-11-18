# this one in Julia for fast matrix manipulation

# Voir PE pb 137 & A081018
# les solutions sont de la forme Fibo(2n)*Fibo(2n+1)

P = 10^9+7
M = Int128[1 1 ; 1 0]

# fast modular exponentiation of matrices
function expo(M,n,p)
  if n==0
    eye(M)
  elseif n%2==0
    (expo(M,div(n,2),p)^2)%p
  else
    (M*(expo(M,div(n-1,2),p)^2)%p)%p
  end
end

T = parse(Int64,readline(STDIN))
for t = 1:T
  N = parse(Int128,readline(STDIN))
  X = expo(M,2*N,P)
  println((X[1,1]*X[1,2])%P)
end
