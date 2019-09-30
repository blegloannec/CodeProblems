// Sqrt-decomposition
#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;

int N,S;
vector<int> A;
vector< vector<int> > R;

void incr(int a, int b, int c) {
  if (b>=S) for (int i=a; i<N; i+=b) A[i] += c;
  else R[b][a] += c;
}

int get(int i) {
  int res = A[i];
  for (int b=1; b<S; ++b) res += R[b][i%b];
  return res;
}

int main() {
  int Q;
  scanf("%d %d", &N, &Q); ++N;
  A.resize(N,0);
  S = (int)sqrt(N)/2.1+1;
  R.resize(S);
  for (int b=1; b<S; ++b) R[b].resize(b,0);
  for (int q=0; q<Q; ++q) {
    int T;
    scanf("%d", &T);
    if (T==1) {
      int a,b,c;
      scanf("%d %d %d", &a, &b, &c);
      incr(a,b,c);
    }
    else {
      int d;
      scanf("%d", &d);
      printf("%d\n", get(d));
    }
  }
  return 0;
}
