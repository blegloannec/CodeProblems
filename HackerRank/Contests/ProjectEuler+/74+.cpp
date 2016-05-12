#include <iostream>
#include <vector>
using namespace std;

int fact[10] = {1,1,2,6,24,120,720,5040,40320,362880};

int f(int n) {
  if (n==0) return 1;
  int res = 0;
  while (n>0) {
    res += fact[n%10];
    n/=10;
  }
  return res;
}

int floyd(int n) {
  // attention a l'init !
  int x = f(n);
  int y = f(f(n));
  while (x!=y) {
    x = f(x);
    y = f(f(y));
  }
  int l0 = 0;
  x = n;
  while (x!=y) {
    x = f(x);
    y = f(y);
    ++l0;
  }
  int l1 = 1;
  y = f(y);
  while (x!=y) {
    y = f(y);
    ++l1;
  }
  return l0+l1;
}

const int Nmax = 1000001;
int C[Nmax];

int main() {
  // using Floyd here is not clever as we finally precompute
  // everything... naive approach with good memo would be better...
  // however this is fast enough
  for (int n=0; n<Nmax; ++n) C[n] = floyd(n);
  int T,N,L;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> N >> L;
    vector<int> res;
    for (int n=0; n<=N; ++n)
      if (C[n]==L) res.push_back(n);
    int s = res.size();
    if (s==0) cout << -1 << endl;
    else {
      cout << res[0];
      for (int i=1; i<s; ++i)
	cout << ' ' << res[i];
      cout << endl;
    }
  }
  return 0;
}
