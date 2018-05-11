#include <iostream>
#include <vector>
using namespace std;

typedef pair<int,int> couple;

const int N = 1000001;
vector<bool> P(N,true);
vector<int> F(N);
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

void decomp(int n, vector<couple> &D) {
  int p = F[n];
  n /= p;
  int m = 1;
  while (n%p==0) {
    n /= p;
    ++m;
  }
  D.push_back(couple(p,m));
  if (n>1) decomp(n,D);
}

int gcd(int a, int b) {
  return b==0 ? a : gcd(b,a%b);
}

int main() {
  sieve_smallest_factor();
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    int n=t;
    cin >> n;
    if (n%4!=0) cout << 0 << endl;
    else {
      vector<couple> D;
      decomp(n,D);
      int p = D[0].second/2, q = D[0].second+1;
      bool sqr = (D[0].second&1)==0;
      for (unsigned int i=1; i<D.size(); ++i) {
	p *= D[i].second/2+1;
	q *= D[i].second+1;
	sqr = sqr && (D[i].second&1)==0;
      }
      --q;
      if (sqr) --p;
      if (p) {
	int g = gcd(p,q);
	cout << p/g << '/' << q/g << endl;
      }
      else cout << 0 << endl;
    }
  }
  return 0;
}
