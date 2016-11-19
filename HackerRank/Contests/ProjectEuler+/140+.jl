# this one in Julia for fast matrix manipulation

# Voir PE pb 140
# on conjecture une relation de recurrence lineaire
# que l'on peut deviner en resolvant un systeme lineaire
# (comme on l'a fait au le pb 324)
# en utilisant Sage pour les calculs, on decouvre la relation
# U(n) = U(n-1) + 7*U(n-2) - 7*U(n-3) - U(n-4) + U(n-5)
# pour la suite de base et
# U(n) = 2*U(n-1) + 6*U(n-2) - 14*U(n-3) + 6*U(n-4) + 2*U(n-5) - U(n-6)
# pour la suite des sommes partielles
# mais une relation de degre 6 est trop lente pour le dernier testcase...
# on remarque qu'en isolant les termes pairs/impairs on a la
# meme relation dans les 2 cas et qu'elle est plus simple (degre 4) :
# U(n) = 9*U(n-1) - 16*U(n-2) + 9*U(n-3) - U(n-4)

P = 10^9+7
M = Int128[9 P-16 9 P-1 ; 1 0 0 0 ; 0 1 0 0 ; 0 0 1 0]
Init1 = Int128[1568 ; 222 ; 28 ; 2]
Init0 = Int128[3605 ; 518 ; 70 ; 7]

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

function S(N)
  if N==0
    0
  elseif N%2==0
    N = div(N,2)
    if N<=4
      Init0[5-N]
    else
      (expo(M,N-4,P)*Init0)[1]%P
    end
  else
    N = div(N+1,2)
    if N<=4
      Init1[5-N]
    else
      (expo(M,N-4,P)*Init1)[1]%P
    end
  end
end

T = parse(Int64,readline(STDIN))
for t = 1:T
  X = split(readline(STDIN))
  L,R = parse(Int64,X[1]),parse(Int64,X[2])
  println((S(R)-S(L-1)+P)%P)
end
