#include <cstdio>
#include <vector>
using namespace std;

vector<int> P;

void sieve(int N) {
  vector<bool> Pr(N,true);
  for (int i=2; i<N; ++i)
    if (Pr[i]) {
      P.push_back(i);
      for (int k=2*i; k<N; k+=i)
	Pr[k] = false;
    }
}

int main() {
  sieve(1<<16);
  int N;
  while (scanf("%d",&N)==1) {
    if (N<0) {
      printf("-1 ");
      N = -N;
    }
    bool first = true;
    int i = 0;
    while (i<(int)P.size() && P[i]*P[i]<=N) {
      if (N%P[i]==0) {
	int m = 1;
	N /= P[i];
	while (N%P[i]==0) {
	  ++m;
	  N /= P[i];
	}
	if (first) first = false;
	else printf(" ");
	printf("%d",P[i]);
	if (m>1) printf("^%d",m);
      }
      ++i;
    }
    if (N>1) {
      if (!first) printf(" ");
      printf("%d",N);
    }
    printf("\n");
  }
  return 0;
}
