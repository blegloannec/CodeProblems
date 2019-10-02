#include <iostream>
#include <vector>
using namespace std;

/*
  Adapté de PE 487.
  f(k,n) = sum( i^k, i=1..n )
  https://en.wikipedia.org/wiki/Faulhaber%27s_formula
  f(k,X) est un polynome de degre k dont on peut calculer
  explicitement les coeff. a partir des nombres de Bernoulli.
  https://en.wikipedia.org/wiki/Bernoulli_number
  Le calcul de ces nombres est en O(k^2).
*/

typedef long long ent;
const int K = 3000;
const ent P = 1000000007;

ent expo(ent a, ent n) {
  if (n==0) return 1;
  if ((n&1)==0) return expo((a*a)%P, n>>1);
  return (a*expo((a*a)%P, n>>1))%P;
}

ent inv_mod(ent a) {
  return expo(a, P-2);
}

vector<ent> F(K+4,1), Finv(K+4,1), Inv(K+4);
void gen_fact() {
  for (ent i=1; i<K+4; ++i) {
    F[i] = (F[i-1]*i) % P;
    Finv[i] = inv_mod(F[i]);
    Inv[i] = inv_mod(i);
  }
}

ent binom(int n, int p) {
  return (F[n] * ((Finv[p]*Finv[n-p])%P)) % P;
}

vector<ent> B(K+3);
void gen_bernoulli() {
  B[0] = 1;
  for (int m=1; m<K+3; ++m) {
    B[m] = 0;
    for (int k=0; k<m; ++k)
      B[m] = (B[m] + ((binom(m,k)*((B[k]*Inv[m-k+1])%P))%P))%P;
    B[m] = (1-B[m]+P)%P;
  }
}

ent f(int m, ent n) {
  ent s = 0;
  for (int k=0; k<=m; ++k)
    s = (s + ((binom(m+1,k)*((B[k]*expo(n,m+1-k))%P))%P))%P;
  s = (s*Inv[m+1])%P;
  return s;
}

int main() {
  gen_fact();
  gen_bernoulli();
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    ent n; int k;
    cin >> n >> k;
    n %= P;
    cout << f(k,n) << endl;
  }
  return 0;
}
