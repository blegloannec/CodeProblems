#include <iostream>
#include <vector>
using namespace std;

// runs in 0.4s with -O3

typedef long long ent;

const int N = 24;
const ent M = 1000000000;
vector<ent> P;

void sieve_list(int N) {
  vector<bool> Pr(N,true);
  for (int i=2; i<N; ++i)
    if (Pr[i]) {
      P.push_back(i);
      for (int k=2*i; k<N; k+=i)
	Pr[k] = false;
    }
}

int main() {
  vector<int> F {0,1};
  for (int i=2; i<=N; ++i) F.push_back(F[i-2]+F[i-1]);
  int S = F[N]+1;
  sieve_list(S);
  
  // prog. dyn.
  vector<ent> DP(S,0);
  DP[0] = 1;
  for (unsigned int i=0; i<P.size(); ++i)
    for (int n=P[i]; n<S; ++n)
      DP[n] = (DP[n] + (DP[n-P[i]]*P[i])%M )%M;
  
  ent res = 0;
  for (int i=2; i<=N; ++i) res = (res+DP[F[i]])%M;
  cout << res << endl;
  return 0;
}
