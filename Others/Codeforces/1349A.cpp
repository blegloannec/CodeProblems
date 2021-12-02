#include <iostream>
#include <vector>
using namespace std;

typedef pair<int,int> couple;

const int N = 200001;

vector<int> F(N);
void sieve_smallest_factor() {
  vector<bool> P(N,true);
  for (long long i=2; i<N; ++i)
    if (P[i]) {
      F[i] = i;
      for (long long k=i*i; k<N; k+=i)
	if (P[k]) {
	  P[k] = false;
	  F[k] = i;
	}
    }
}

vector<couple> decomp(int n) {
  vector<couple> D;
  while (n>1) {
    int p = F[n], m = 0;
    while (n%p==0) {++m; n /= p;}
    D.push_back(make_pair(p,m));
  }
  return D;
}

int main() {
  sieve_smallest_factor();
  int n;
  cin >> n;
  vector<int> Cnt(N,0), Min(N,N), SndMin(N,N);
  for (int i=0; i<n; ++i) {
    int s;
    cin >> s;
    vector<couple> D = decomp(s);
    for (const couple& pm : D) {
      int p = pm.first, m = pm.second;
      ++Cnt[p];
      if (m<=Min[p]) {
	SndMin[p] = Min[p];
	Min[p] = m;
      }
      else if (m<SndMin[p]) SndMin[p] = m;
    }
  }
  long long res = 1;
  for (int p=2; p<N; ++p)
    if (Cnt[p]>=n-1) {
      int m = Cnt[p]==n ? SndMin[p] : Min[p];
      for (int k=0; k<m; ++k) res *= p;
    }
  cout << res << endl;
  return 0;
}
