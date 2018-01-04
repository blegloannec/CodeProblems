#include <iostream>
#include <vector>
using namespace std;

typedef unsigned long long ent;

vector<ent> P;

void sieve_list(ent N) {
  vector<bool> Pr(N,true);
  for (ent i=2; i<N; ++i)
    if (Pr[i]) {
      P.push_back(i);
      for (ent k=2*i; k<N; k+=i)
	Pr[k] = false;
    }
}

// crible pour marquer les nb premiers L <= n <= R
vector<bool> prime_int(ent L, ent R) {
  vector<bool> D(R-L+1,true);
  for (vector<ent>::iterator ip=P.begin(); ip!=P.end() && (*ip)*(*ip)<=R; ++ip) {
    ent p = *ip;
    for (ent n=max(2LLu,(L+p-1)/p)*p; n<=R; n+=p) D[n-L] = false;
  }
  return D;
}

ent expmod(ent x, ent n, ent m) {
  if (n==0) return 1;
  if ((n&1)==0) return expmod((x*x)%m,n>>1,m);
  return (x*expmod((x*x)%m,n>>1,m))%m;
}

bool suspect(ent b, ent n) {
  ent u = n-1;
  int t = 0;
  while ((u&1)==0) {
    ++t;
    u >>= 1;
  }
  ent x = expmod(b,u,n);
  for (int i=1; i<=t; ++i) {
    ent x0 = x;
    x = (x*x)%n;
    if (x==1 && x0!=1 && x0!=n-1) return false;
  }
  return (x==1);
}

int main() {
  sieve_list(1<<16);
  ent b,L,R;
  bool first = true;
  cin >> b >> L >> R;
  while (b) {
    if (first) first = false;
    else cout << endl;
    vector<bool> P = prime_int(L,R);
    int cpt = 0;
    vector<ent> S;
    for (ent i=L+1-(L&1); i<=R; i+=2)
      if (!P[i-L]) {
	++cpt;
	if (suspect(b,i)) S.push_back(i);
      }
    cout << "There are " << cpt << " odd non-prime numbers between " << L << " and " << R << "." << endl;
    if (!S.empty()) {
      cout << S.size() << " suspects fail in base " << b << ":" << endl;
      for (vector<ent>::iterator it=S.begin(); it!=S.end(); ++it)
	cout << *it << endl;
    }
    else cout << "There are no failures in base " << b << "." << endl;
    cin >> b >> L >> R;
  }
  return 0;
}
