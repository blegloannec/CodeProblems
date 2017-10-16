#include <cstdio>
#include <vector>
using namespace std;

typedef long long ent;

int N;
vector<int> A;
vector< vector<ent> > W;
vector< pair<int,int> > P;
vector<ent> C;

ent cycle_dist(int i, int u, int v) {
  if (u>v) swap(u,v);
  return min(W[i][v]-W[i][u],W[i][A[i]]-W[i][v]+W[i][u]);
}

int Cindex(int c, bool first) {
  if (c==0) return first ? (int)C.size()-2 : 0;
  else return 1 + 2*(c-1) + (first ? 0 : 1);
}

ent out_dist(int u, int v) {
  if (u>v) swap(u,v);
  return min(C[v]-C[u],C[(int)C.size()-1]-C[v]+C[u]);
}

ent dist(int v1, int c1, int v2, int c2) {
  return min(min(cycle_dist(c1,v1,P[c1].first)+out_dist(Cindex(c1,true),Cindex(c2,true))+cycle_dist(c2,P[c2].first,v2),
		 cycle_dist(c1,v1,P[c1].first)+out_dist(Cindex(c1,true),Cindex(c2,false))+cycle_dist(c2,P[c2].second,v2)),
	     min(cycle_dist(c1,v1,P[c1].second)+out_dist(Cindex(c1,false),Cindex(c2,true))+cycle_dist(c2,P[c2].first,v2),
		 cycle_dist(c1,v1,P[c1].second)+out_dist(Cindex(c1,false),Cindex(c2,false))+cycle_dist(c2,P[c2].second,v2)));
}

int main() {
  int T;
  scanf("%d",&T);
  for (int t=0; t<T; ++t) {
    int Q;
    scanf("%d %d",&N,&Q);
    A.resize(N);
    W.resize(N);
    for (int i=0; i<N; ++i) {
      scanf("%d",&A[i]);
      W[i].resize(A[i]+1,0);
      for (int j=1; j<=A[i]; ++j) {
	scanf("%lld",&W[i][j]);
	W[i][j] += W[i][j-1];
      }
    }
    P.resize(N);
    C.resize(1,0);
    for (int i=0; i<N; ++i) {
      int v1,v2,w;
      scanf("%d %d %d",&v1,&v2,&w); --v1; --v2;
      P[i].second = v1;
      P[(i+1)%N].first = v2;
      if (i>0) C.push_back(C[(int)C.size()-1]+cycle_dist(i,P[i].first,P[i].second));
      C.push_back(C[(int)C.size()-1]+w);
    }
    C.push_back(C[(int)C.size()-1]+cycle_dist(0,P[0].first,P[0].second));
    for (int q=0; q<Q; ++q) {
      int v1,c1,v2,c2;
      scanf("%d %d %d %d",&v1,&c1,&v2,&c2);
      --v1; --c1; --v2; --c2;
      printf("%lld\n",dist(v1,c1,v2,c2));
    }
    // cleaning
    A.clear();
    W.clear();
    P.clear();
    C.clear();
  }
  return 0;
}
