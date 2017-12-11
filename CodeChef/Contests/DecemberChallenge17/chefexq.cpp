#include <cstdio>
#include <vector>
#include <unordered_map>
#include <cmath>
using namespace std;

int N,Q,BS,S;
vector<int> A,P,X;
vector< unordered_map<int,int> > B;

void update(int b) {
  B[b].clear();
  X[b] = 0;
  P[b*S] = A[b*S] ^ (b==0 ? 0 : P[b*S-1]^X[b-1]);
  ++B[b][P[b*S]];
  for (int i=b*S+1; i<min((b+1)*S,N); ++i) {
    P[i] = P[i-1] ^ A[i];
    ++B[b][P[i]];
  }
}

int find(int b, int k) {
  k ^= X[b];
  auto it = B[b].find(k);
  return (it==B[b].end() ? 0 : it->second);
}

int main() {
  scanf("%d %d",&N,&Q);
  A.resize(N);
  P.resize(N);
  for (int i=0; i<N; ++i) scanf("%d",&A[i]);
  S = (int)sqrt(N)+1;
  BS = (N+S-1)/S;
  B.resize(BS);
  X.resize(BS,0);
  for (int b=0; b<BS; ++b) update(b);
  for (int q=0; q<Q; ++q) {
    int t,i,k;
    scanf("%d %d %d",&t,&i,&k); --i;
    int b = i/S;
    if (t==1) {
      int x0 = A[i]^k;
      A[i] = k;
      update(b);
      for (int c=b+1; c<BS; ++c) X[c] ^= x0;
    }
    else {
      int cpt = 0;
      for (int c=0; c<b; ++c) cpt += find(c,k);
      for (int j=b*S; j<=i; ++j)
	if ((X[b]^P[j])==k) ++cpt;
      printf("%d\n",cpt);
    }
  }
  return 0;
}
