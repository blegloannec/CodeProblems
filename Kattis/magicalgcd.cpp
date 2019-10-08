#include <cstdio>
#include <vector>
using namespace std;
using ll = long long;

int N;
vector<ll> A;

ll gcd(ll a, ll b) {
  return b==0 ? a : gcd(b,a%b);
}

ll magical_gcd() {
  ll res = -1;
  vector<int> Sidx;
  vector<ll> Sgcd;
  /*
    After the i-th iteration, Sgcd contains the list of GCDs,
    without duplicates, of segments ending at index i.
    Sidx contains the corresponding smallest starting indexes.
    Because each element of Sgcd is a strict divisor of the next element,
    the size of Sgcd is bounded by 40 > log2 10^12.
  */
  for (int i=0; i<N; ++i) {
    // updating GCDs
    for (int j=(int)Sidx.size()-1; j>=0; --j)
      Sgcd[j] = gcd(Sgcd[j], A[i]);
    Sidx.push_back(i);
    Sgcd.push_back(A[i]);
    // removing duplicates and updating result
    vector<int> NewSidx;
    vector<ll> NewSgcd;
    for (int j=0; j<(int)Sidx.size(); ++j)
      if (j==0 || Sgcd[j]!=Sgcd[j-1]) {
	NewSidx.push_back(Sidx[j]);
	NewSgcd.push_back(Sgcd[j]);
	res = max(res, (i-Sidx[j]+1)*Sgcd[j]);
      }
    swap(Sidx, NewSidx);
    swap(Sgcd, NewSgcd);
  }
  return res;
}

int main() {
  int T;
  scanf("%d", &T);
  for (int t=0; t<T; ++t) {
    scanf("%d", &N);
    A.resize(N);
    for (int i=0; i<N; ++i) scanf("%lld", &A[i]);
    printf("%lld\n", magical_gcd());
  }
  return 0;
}
