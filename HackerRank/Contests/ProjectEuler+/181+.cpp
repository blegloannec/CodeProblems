#include <cstdio>
#include <vector>
using namespace std;

/*
  implementation efficace (en memoire, seulement O(N^2) en faisant
  les operations dans le bon ordre) de la prog. dyn. du 181.py
*/

const int P = 1000000007;
const int MAX = 160;
vector< vector<int> > G(MAX+1);

inline void incr(int &x, int y) {
  x += y;
  if (x>=P) x -= P;
}

void dp() {
  for (int i=0; i<=MAX; ++i) G[i].resize(MAX+1,0);
  G[0][0] = 1;
  for (int M=1; M<=2*MAX; ++M)
    for (int b=0; b<=M; ++b) {
      int w = M-b;
      for (int B=b; B<=MAX; ++B)
	for (int W=w; W<=MAX; ++W)
	  incr(G[B][W],G[B-b][W-w]);
    }
}

int main() {
  int Q,B,W;
  dp();
  scanf("%d",&Q);
  for (int q=0; q<Q; ++q) {
    scanf("%d %d",&B,&W);
    printf("%d\n",G[B][W]);
  }
  return 0;
}
