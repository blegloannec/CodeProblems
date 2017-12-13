// pb 1137 on UVa, 2946 on Archive
#include <iostream>
#include <vector>
using namespace std;

vector<int> P;

void sieve(int n) {
  vector<bool> B(n,true);
  for (int i=2; i<n; ++i)
    if (B[i]) {
      P.push_back(i);
      for (int k=2*i; k<n; k+=i)
	B[k] = false;
    }
}

vector<int> phonies(int l, int r) {
  vector<int> res;
  if (r<l) return res;
  int S = r-l+1;
  vector<int> N(S),nb_fact(S,0);
  vector<bool> phony(S,true);
  for (int i=0; i<S; ++i) N[i] = l+i;
  for (auto ip=P.begin(); ip!=P.end() && *ip<=r; ++ip) {
    int p = *ip;
    for (long long k=((l+p-1)/p)*p; k<=r; k+=p) {
      int i = k-l;
      if (phony[i]) {
	if (k%(p*p)==0 || (k-1)%(p-1)!=0) phony[i] = false;
	else {
	  N[i] /= p;
	  ++nb_fact[i];
	}
      }
    }
  }
  for (int i=0; i<S; ++i)
    if (phony[i]) {
      int n = l+i;
      if (N[i]>1) {
	++nb_fact[i];
	if ((n-1)%(N[i]-1)!=0) phony[i] = false;
      }
      if (phony[i] && nb_fact[i]>=3)
	res.push_back(n);
    }
  return res;
}

int main() {
  sieve(1<<16);
  int l,r;
  bool first = true;
  while (cin >> l >> r) {
    if (!first) cout << endl;
    else first = false;
    vector<int> phony = phonies(l,r);
    if (phony.empty()) cout << "none" << endl;
    else
      for (auto it=phony.begin(); it!=phony.end(); ++it)
	cout << *it << endl;
  }
  return 0;
}
