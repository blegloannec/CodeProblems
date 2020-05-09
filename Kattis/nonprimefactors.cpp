#include <cstdio>
#include <vector>
using namespace std;

const int N = 2000001;
vector<bool> P(N,true);
vector<int> F(N,1), PF(N,0);

void sieve_factors() {
  for (long long i=2; i<N; ++i)
    if (P[i]) {
      F[i] = 2;
      PF[i] = 1;
      for (int k=2*i; k<N; k+=i) {
	P[k] = false;
	++PF[k];
	F[k] *= 2;
      }
      int m = 2;
      long long j = i*i;
      while (j<N) {
	for (int k=j; k<N; k+=j)
	  F[k] = (F[k]/m)*(m+1);
	++m;
	j *= i;
      }
    }
}

int main() {
  sieve_factors();
  int Q;
  scanf("%d", &Q);
  for (int q=0; q<Q; ++q) {
    int n;
    scanf("%d", &n);
    int res = F[n] - PF[n];
    printf("%d\n", res);
  }
  return 0;
}
