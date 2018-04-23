#include <cstdio>
#include <vector>
using namespace std;

const int N = 100000;
const int S = 317;

int T[S][S];
vector<int> M(N+1,0);

void init() {
  for (int a=1; a<S; ++a)
    for (int b=0; b<a; ++b) T[a][b] = 0;
}

void mark(int a, int b, int d) {
  for (int k=b; k<=N; k+=a) M[k] += d;
  for (int k=b-a; k>=0; k-=a) M[k] += d;
}

int count(int q) {
  int res = M[q];
  for (int a=1; a<S; ++a) res += T[a][q%a];
  return res;
}

int main() {
  init();
  int n;
  scanf("%d",&n);
  for (int t=0; t<n; ++t) {
    char c;
    scanf(" %c",&c);
    if (c=='?') {
      int q;
      scanf("%d",&q);
      printf("%d\n",count(q));
    }
    else {
      int a,b;
      scanf("%d %d",&a,&b);
      int d = (c=='+' ? 1 : -1);
      if (a<S) T[a][b%a] += d;
      else mark(a,b,d);
    }
  }
  return 0;
}
