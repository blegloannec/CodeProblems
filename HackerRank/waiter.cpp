/*
  O(M log(log M) + N + Q) approach for M = 10^4 the nb bound
  the editorial actually expected a naive O(N*Q) approach...
*/
#include <iostream>
#include <vector>
using namespace std;

const int N = 10001;
vector<bool> P(N,true);
vector<int> F(N),L;

void sieve_smallest_factor_index() {
  int cnt = 0;
  P[0] = P[1] = false;
  for (int i=2; i<N; ++i)
    if (P[i]) {
      F[i] = cnt;
      for (int k=2*i; k<N; k+=i)
	if (P[k]) {
	  P[k] = false;
	  F[k] = cnt;
	}
      ++cnt;
    }
}

int main() {
  sieve_smallest_factor_index();
  int n,Q;
  cin >> n >> Q;
  vector< vector<int> > C(Q+1);
  for (int i=0; i<n; ++i) {
    int x;
    cin >> x;
    C[min(F[x],Q)].push_back(x);
  }
  for (int q=0; q<=Q; ++q) {
    if ((q==Q?Q-1:q)%2==0)
      for (auto it=C[q].begin(); it!=C[q].end(); ++it)
	cout << *it << endl;
    else
      for (auto it=C[q].rbegin(); it!=C[q].rend(); ++it)
	cout << *it << endl;
  }
  return 0;
}
