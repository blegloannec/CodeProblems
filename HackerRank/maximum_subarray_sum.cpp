#include <iostream>
#include <vector>
#include <set>
using namespace std;
using ll = long long;

int N;
ll M;
vector<ll> A;
set<ll> Pref;

int main() {
  int Q;
  cin >> Q;
  for (int q=0; q<Q; ++q) {
    cin >> N >> M;
    A.resize(N);
    for (int i=0; i<N; ++i) cin >> A[i];
    Pref.insert(0);  // empty prefix
    ll S = 0, res = 0;
    for (int i=0; i<N; ++i) {
      // current prefix sum(A[0..i])%M
      S = (S+A[i]) % M;
      res = max(S,res);
      // smallest prefix sum(A[0..j])%M > sum(A[0..i])%M for j < i
      // then sum(A[i+1..j])%M is the best candidate
      auto it = Pref.upper_bound(S);  
      if (it!=Pref.end()) res = max(res,S+M-*it);
      Pref.insert(S);
    }
    cout << res << endl;
    // cleaning
    Pref.clear();
  }
  return 0;
}
