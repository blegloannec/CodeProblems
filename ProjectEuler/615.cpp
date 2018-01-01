#include <iostream>
#include <vector>
#include <cmath>
#include <set>
#include <unordered_set>
using namespace std;

// runs in 5s with -O3

typedef long long ent;

const ent M = 123454321;
vector<int> P;
vector<double> L;

const ent BH = 2000001;
const ent PH = 333333333333333331LL;
vector<ent> BHpow;

ent expmod(ent x, ent n, ent m=M) {
  if (!n) return 1;
  if (!(n&1)) return expmod((x*x)%m,n>>1,m);
  return (x*expmod((x*x)%m,n>>1,m))%m;
}

struct decomp {
  vector<int> D;
  double l;
  ent h;
  
  decomp(int n) {
    D.resize(1,n);
    l = n*L[0];
    h = n;
  }
  
  ent valmod() const {
    ent v = 1;
    for (unsigned int i=0; i<D.size(); ++i)
      v = (v*expmod(P[i],D[i]))%M;
    return v;
  }
  
  bool operator<(const decomp &B) const {
    return this->l < B.l;
  }
};

void sieve_list(int N) {
  vector<bool> Pr(N,true);
  for (int i=2; i<N; ++i)
    if (Pr[i]) {
      P.push_back(i);
      for (int k=2*i; k<N; k+=i)
	Pr[k] = false;
    }
}

ent nth(int n) {
  set<decomp> H;
  unordered_set<ent> seen;
  for (int i=0; i<n; ++i) {
    decomp d(n+i);
    H.insert(d);
    seen.insert(d.h);
  }
  for (int i=0; i<n-1; ++i) {
    decomp A = *H.begin();
    H.erase(H.begin());
    for (int i=0; i<(int)A.D.size(); ++i)
      if (A.D[i]>0) {
	decomp B = A;
	if (i==(int)A.D.size()-1) B.D.push_back(0);
	--B.D[i]; ++B.D[i+1];
	B.l += L[i+1] - L[i];
	B.h = (B.h + BHpow[i+1] - BHpow[i])%PH;
	if (B.l < H.rbegin()->l && seen.find(B.h)==seen.end()) {
	  H.insert(B);
	  seen.insert(B.h);
	  auto last = H.end(); --last;
	  if ((int)H.size()>n-i) H.erase(last);
	}
      }
  }
  return H.begin()->valmod();
}

int main() {
  sieve_list(500000);
  L.resize(P.size());
  for (unsigned int i=0; i<P.size(); ++i)
    L[i] = log(P[i]);
  BHpow.resize(P.size(),1);
  for (unsigned int i=1; i<P.size(); ++i)
    BHpow[i] = (BHpow[i-1]*BH)%PH;
  cout << nth(1000000) << endl;
  return 0;
}
