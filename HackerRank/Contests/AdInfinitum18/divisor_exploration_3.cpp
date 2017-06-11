#include <iostream>
#include <vector>
using namespace std;

typedef long long ent;
const ent P = 1000000007;
vector<ent> F(3005,1),Finv(3005,1),Pr;

ent bezout(ent a, ent b, ent &u, ent &v) {
  if (b==0) {
    u = 1;
    v = 0;
    return a;
  }
  ent u1,v1;
  ent g = bezout(b,a%b,u1,v1);
  u = v1;
  v = u1-(a/b)*v1;
  return g;
}

ent inv_mod(ent a, ent n=P) {
  ent u,v;
  bezout(a,n,u,v);
  return (u+n)%n;
}

ent binom(int n, int p) {
  return (F[n]*((Finv[p]*Finv[n-p])%P))%P;
}

void sieve_list(int N) {
  vector<bool> P(N,true);
  for (int i=2; i<N; ++i)
    if (P[i]) {
      Pr.push_back(i);
      for (int k=2*i; k<N; k+=i) P[k] = false;
    }
}

ent explo(int m, int a, int d) {
  ent S = 1;
  for (int i=0; i<m; ++i) {
    ent p = Pr[i];
    int x = a+i+1;
    ent S0 = (S*binom(d+x,x))%P;
    ent y = 0;
    for (int j=0; j<x; ++j) y = (((p*y)%P) + binom(d+j,j))%P;
    ent S1 = (y*((S*(p-1))%P))%P;
    S = (S0+S1)%P;
  }
  return S;
}

int main() {
  for (ent i=1; i<3005; ++i) {
    F[i] = (F[i-1]*i)%P;
    Finv[i] = inv_mod(F[i])%P;
  }
  sieve_list(8000);
  int q,m,a,d;
  cin >> q;
  for (int i=0; i<q; ++i) {
    cin >> m >> a >> d;
    cout << explo(m,a,d-1) << endl;
  }
  return 0;
}
