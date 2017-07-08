#include <iostream>
#include <vector>
using namespace std;

/*
  par exemple pour N = 11, on peut prendre les pentes
  successives 1/3, 1/2, 1/1, 3/2, 2/1, 3/1
  ce qui donne 7 points de l'optimum partant de (0,0)
  pour F(n), il s'agit de trouver un plus grand ensemble
  de fractions irreductibles distinctes telles que
  la somme des numerateurs (deplacement vertical) et la somme
  des denominateurs (deplacement horizontal) soient <= N
  (pour construire la "courbe" correspondante, on trierait les fractions)
  pour l'exemple 1+1+1+3+2+3 = 11 et 3+2+1+2+1+1 = 10
  la sequence partant de (0,0) aboutit en (10,11) <= (11,11)
  
  une fraction a/b contribue d'autant moins que a+b est faible, on
  considere donc les fractions dans cet ordre
  pour x fixe, si l'on connait C(x) le nb de fractions irreductibles a/b
  avec a+b = x, alors leur contribution (verticale/horizontale)
  totale est C(x)*x/2
  des lors, si l'on sait calculer efficacement C(), on peut traiter
  toutes ces fractions d'un coup ce qui permet d'arriver tres vite
  au x limite pour lequel on ajoute les fractions une a une jusqu'a
  arriver a N
  essentiellement, c'est un algo glouton tres accelere

  C(x) = nb de couples (a,b) tq a+b = x et gcd(a,b) = 1
  mais gcd(a,b) = gcd(a,b+a) = gcd(a,x) donc C(x) = phi(x)

  runs in 0.15s with -03
*/

typedef long long ll;

const int N = 2500000;
vector<bool> P(N,true);
vector<int> Phi(N,1);

void sieve_totient() {
  P[0] = P[1] = false;
  for (int i=2; i<N; ++i)
    if (P[i]) {
      Phi[i] = i-1;
      for (int k=2*i; k<N; k+=i) {
	P[k] = false;
	int m = 1;
	int l = k/i;
	while (l%i==0) {
	  l /= i;
	  m *= i;
	}
	Phi[k] *= (i-1)*m;
      }
    }
}

int gcd(int a, int b) {
  return b==0 ? a : gcd(b,a%b);
}

ll F(ll n) {
  ll s = 1, ab = 3, f = 1;
  while (s<=n) {
    if (s+(Phi[ab]*ab)/2<=n) {
      // on traite d'un coup toutes les fractions a/b tq a+b = ab
      f += Phi[ab];
      s += (Phi[ab]*ab)/2;
    }
    else {
      // on les parcourt une a une jusqu'a arriver a s > n
      for (int a=1; a<=ab/2; ++a) {
	int b = ab-a;
	if (a==b) continue;
	if (gcd(a,b)==1) {
	  ++f;
	  s += a;
	  if (s>n) break;
	  ++f;
	  s += b;
	  if (s>n) break;
	}
      }
    }
    ++ab;
  }
  return f;
}

int main() {
  sieve_totient();
  const ll n = 1000000000000000000LL; // input 10^18
  cout << F(n) << endl;
  return 0;
}
