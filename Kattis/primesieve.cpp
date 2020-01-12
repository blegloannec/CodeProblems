#include <cstdio>
#include <vector>
using namespace std;

int N;
vector<bool> P;

int sieve() {
  int cpt = 0;
  P.resize(N+1,true);
  P[0] = P[1] = false;
  for (long long i=2; i<=N; ++i)
    if (P[i]) {
      ++cpt;
      for (long long k=2*i; k<=N; k+=i)
	P[k] = false;
    }
  return cpt;
}

int main() {
  int Q;
  scanf("%d %d",&N,&Q);
  int cpt = sieve();
  printf("%d\n",cpt);
  for (int q=0; q<Q; ++q) {
    int x;
    scanf("%d",&x);
    printf("%d\n",(int)P[x]);
  }
  return 0;
}
