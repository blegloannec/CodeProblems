#include <iostream>
#include <vector>
using namespace std;

typedef long long ent;

/*
  Some related references for partial orders:
  https://en.wikipedia.org/wiki/Mirsky%27s_theorem
  max length of a chain = min size of a partition into antichains
  https://en.wikipedia.org/wiki/Dilworth%27s_theorem
  max size of an antichain = min size of a partition into chains
  https://en.wikipedia.org/wiki/Birkhoff%27s_representation_theorem
  to represent the divisibility lattice as a set lattice (obvious, take the
  sub-multisets of the primal decomposition)
  Here the largest antichain in the divisors lattice of n is rather clearly
  obtained by taking the antichain of divisors having k/2 primes factors
  (taking multiplicity into account) for k the number of prime factors of
  n (multiplicity included). If k is odd, using (k-1)/2 or (k+1)/2 is
  equivalent.
  If all primes factors are distinct, it is then binom(k,k/2).
  Hovewer, with multiplicities, you have to remove duplicates.
  We do a DP here (don't know if there is a nice formula)...

  runs in ~20s with -O
*/

const int N = 100000001;
vector<bool> P(N,true);
vector<int> F(N);
const int DPS = 30;
int DP[DPS][DPS];

int dp(vector<int> &M, int K) {
  for (int i=1; i<=(int)M.size(); ++i)
    for (int k=0; k<=K; ++k) {
      DP[i][k] = 0;
      for (int j=0; j<=M[i-1] && j<=k; ++j)
	DP[i][k] += DP[i-1][k-j];
    }
  return DP[M.size()][K];
}

ent binom(ent n, ent p) {
  return p==0?1:n*binom(n-1,p-1)/p;
}

void sieve_smallest_factor() {
  P[0] = P[1] = false;
  for (int i=2; i<N; ++i)
    if (P[i]) {
      F[i] = i;
      for (int k=2*i; k<N; k+=i)
	if (P[k]) {
	  P[k] = false;
	  F[k] = i;
	}
    }
}

int multiplicities(int n, vector<int> &M) {
  int s = 0;
  while (n>1) {
    int p = F[n];
    n /= p;
    int m = 1;
    while (n%p==0) {
      n /= p;
      ++m;
    }
    s += m;
    M.push_back(m);
  }
  return s;
}

int main() {
  DP[0][0] = 1;
  for (int k=1; k<DPS; ++k)
    DP[0][k] = 0;
  sieve_smallest_factor();
  ent S = 0;
  for (int n=1; n<N; ++n) {
    vector<int> M;
    int k = multiplicities(n,M);
    S += dp(M,k/2);
  }
  cout << S << endl;
  return 0;
}
