#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

// O(Q sqrt(N) log(sqrt(N))) square-root decomposition approach

int N,Q,S,BS;
vector<int> A;
vector< vector<int> > B;

void pass(int l, int r, vector<int> &Q) {
  Q.clear();
  Q.push_back(A[l]);
  for (int i=l+1; i<=r; ++i)
    if (Q[(int)Q.size()-1]<A[i]) Q.push_back(A[i]);
}

void block_pass(int i) {
  pass(i*S,min((i+1)*S-1,N-1),B[i]);
}

int count(int i, int L, int R) {
  int h = L-1, b0 = i/S;
  vector<int> Q0;
  pass(i,min((b0+1)*S-1,N-1),Q0);
  auto l = upper_bound(Q0.begin(),Q0.end(),h);
  int hmax = Q0[(int)Q0.size()-1];
  if (hmax>=R) {
    auto r = lower_bound(Q0.begin(),Q0.end(),R);
    return distance(l,r)+1;
  }
  int cpt = distance(l,Q0.end());
  h = max(h,hmax);
  for (int b=b0+1; b<BS; ++b) {
    auto l = upper_bound(B[b].begin(),B[b].end(),h);
    int hmax = B[b][(int)B[b].size()-1];
    if (hmax>=R) {
      auto r = lower_bound(B[b].begin(),B[b].end(),R);
      return cpt+distance(l,r)+1;
    }
    cpt += distance(l,B[b].end());
    h = max(h,hmax);
  }
  return cpt;
}

int main() {
  int T;
  scanf("%d",&T);
  for (int t=0; t<T; ++t) {
    scanf("%d %d",&N,&Q);
    A.resize(N);
    for (int i=0; i<N; ++i) scanf("%d",&A[i]);
    S = (int)sqrt(N)+1;
    BS = (N+S-1)/S;
    B.resize(BS);
    for (int i=0; i<BS; ++i) block_pass(i);
    for (int q=0; q<Q; ++q) {
      char c; int i;
      scanf(" %c %d",&c,&i); --i;
      if (c=='+') {
	int X;
	scanf("%d",&X);
	A[i] += X;
	block_pass(i/S);
      }
      else {
	int L,R;
	scanf("%d %d",&L,&R);
	printf("%d\n",count(i,L,R));
      }
    }
  }
  return 0;
}
