#include <iostream>
#include <vector>
using namespace std;

/*
  posons q(n,k) = nb de pi-sequences u pour lesquelles u0 = n et c(u) = k
  p(n,k) = sum( q(m,k), m<=n ) est le cumul des q(n,.)
  q(n,k) = q(pi(n),k)   + e(n,k)  si n est premier
         = q(pi(n),k-1) + e(n,k)  sinon
  ou e(n,k) est le terme comptant la nouvelle sequence de taille 2 (n,pi(n))
  e(n,k) = 1 si n et pi(n) sont premiers et k = 0
         = 1 si soit n, soit pi(n) est premier et k = 1
         = 1 si n et pi(n) ne sont pas premiers et k = 2
         = 0 sinon

  runs in ~5s with -O3
*/

const int N = 100000000;
const int M = 1000000007;
vector<bool> P(N+1,true);

void sieve() {
  P[0] = P[1] = false;
  for (int i=2; i*i<=N; ++i)
    if (P[i])
      for (int k=2*i; k<=N; k+=i)
	P[k] = false;
}

int main() {
  sieve();
  int Pi = 0;
  for (int n=2; n<=N; ++n) if (P[n]) ++Pi;
  vector< vector<short> > q(2);
  q[1].resize(3,0);
  vector<int> p(15,0);
  int pi = 0;
  for (int n=2; n<=N; ++n) {
    vector<short> qn;
    if (P[n]) {
      ++pi;
      qn = q[pi]; // copie
    }
    else {
      qn.resize((int)q[pi].size()+1);
      for (int k=1; k<(int)qn.size(); ++k)
	qn[k] = q[pi][k-1];
    }
    ++qn[(P[n]?0:1)+(P[pi]?0:1)];
    for (int k=0; k<(int)qn.size(); ++k) p[k] += qn[k];
    if (n<=Pi) q.push_back(qn);
  }
  long long res = 1;
  for (int k=0; k<(int)p.size(); ++k)
    if (p[k]>0) res = (res*p[k])%M;
  cout << res << endl;
  return 0;
}
