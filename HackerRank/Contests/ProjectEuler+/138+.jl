# this one in Julia for fast matrix manipulation

# Voir PE pb 138
# On remarque que les solutions verifient l'equation
# L(n) = 18*L(n-1) - L(n-2)
# avec les valeurs initiales 17 et 305
# Soit S(n) = sum( L(i), i<=n )
# S(n) = L(n) + S(n-1)
#      = 18*L(n-1) - L(n-2) + S(n-1)
#      = 18*(S(n-1)-S(n-2)) - (S(n-2)-S(n-3)) + S(n-1)
#      = 19*S(n-1) - 19*S(n-2) + S(n-3)
# Valeurs initiales : 17, 322, 5795

P = 10^9+7
M = Int128[19 P-19 1 ; 1 0 0 ; 0 1 0]
I = Int128[5795 ; 322 ; 17]

# fast modular exponentiation of matrices
function expo(M,n,p)
  if n==0
    eye(M)
  elseif n%2==0
    (expo(M,(n//2).num,p)^2)%p
  else
    (M*(expo(M,((n-1)//2).num,p)^2)%p)%p
  end
end

T = parse(Int64,readline(STDIN))
for t = 1:T
  N = parse(Int128,readline(STDIN))
  if N==1
    println(17)
   elseif N==2
     println(322)
   else
     println(((expo(M,N-3,P)*I)%P)[1])
   end
end
