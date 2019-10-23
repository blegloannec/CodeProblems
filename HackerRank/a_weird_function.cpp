/*
  function(L,R) = sum of the euler_phi(i) for each triangular number i
                  (i.e. i = j(j+1)/2) between L and R
  /!\ euler_phi(1) = 1
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using ll = long long;

const int JMAX = 2000000;
const ll  RMAX = 1000000000000LL;

vector<int> Phi;
vector<ll> Triang {0}, SumPhiTriang {0};

void sieve_totient(int N) {
  vector<bool> P(N, true);
  Phi.resize(N);
  for (int i=0; i<N; ++i) Phi[i] = i;
  for (int i=2; i<N; ++i)
    if (P[i]) {
      Phi[i] = i-1;
      for (int k=2*i; k<N; k+=i) {
	P[k] = false;
	Phi[k] = (i-1)*(Phi[k]/i);
      }
    }
}

ll phi_triang(int j) { // phi(j(j+1)/2)
  ll res = (ll)Phi[j] * (ll)Phi[j+1];
  if (j%4==0 || (j+1)%4==0) res /= 2;
  return res;
}

ll pref_sum(ll R) {
  int i = distance(Triang.begin(), upper_bound(Triang.begin(), Triang.end(), R));
  return SumPhiTriang[i-1];
}

int main() {
  sieve_totient(JMAX);
  for (ll j=1; j*(j+1)/2<=RMAX; ++j) {
    Triang.push_back(j*(j+1)/2);
    SumPhiTriang.push_back(SumPhiTriang.back() + phi_triang(j));
  }
  int T;
  cin >> T;
  for (int i=0; i<T; ++i) {
    ll L,R;
    cin >> L >> R;
    cout << pref_sum(R)-pref_sum(L-1) << '\n';
  }
  return 0;
}
