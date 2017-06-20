#include <iostream>
#include <vector>
using namespace std;

/*
  https://en.wikipedia.org/wiki/Faulhaber%27s_formula
  a1(k) est (au signe pres) le k-ieme nombre de Bernoulli
  https://en.wikipedia.org/wiki/Von_Staudt%E2%80%93Clausen_theorem
  son denominateur verifie D(2k+1) = 1
  et D(2k) = prod( p premier tq p-1 | 2k )
  ici on cherche les k (pairs) tq D(k) = 20010 = 2*3*5*23*29
  ie les k tq 4 | k, 22 | k et 28 | k
  donc k est multiple de 4*7*11 mais n'est divisible par aucun p-1
  pour p premier different de 2, 3, 5, 23 et 29
  on peut simplement cribler ces nombres

  runs in 15s with -O3
*/

const int N = 1000000000;
const int K = 4*7*11;
const int M = N/K+1;
vector<bool> P(N,true),L(M,true);

int gcd(int a, int b) {
  return b==0 ? a : gcd(b,a%b);
}

void sieve() {
  for (int i=2; i<N; ++i)
    if (P[i]) {
      if (i>5 && i!=23 && i!=29) {
	// on marque les multiples de i-1 parmi les multiples de K
	int j = (i-1)/gcd(K,i-1);
	for (int k=j; k<M; k+=j) L[k] = false;
      }
      for (int k=2*i; k<N; k+=i) P[k] = false;
    }
}

int main() {
  sieve();
  int i = 0, cpt = 0;
  while (cpt<100000) if (L[++i]) ++cpt;
  cout << i*K << endl;
  return 0;
}
