#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

#define _v_ first
#define _t_ second

int K,N,B;
vector< vector< pair<int,int> > > G;
vector< vector<int> > MidDist;

vector<int> dp_all_dist(int start) {
  vector<int> D(N,-1);
  D[start] = 0;
  for (int u=start+1; u<N; ++u)
    for (const auto &e : G[u]) {
      int v = e._v_, t = e._t_;
      if (v<u && v>=start && D[v]>=0 && (D[u]<0 || D[v]+t<D[u]))
	D[u] = D[v]+t;
    }
  for (int u=start-1; u>=0; --u)
    for (const auto &e : G[u]) {
      int v = e._v_, t = e._t_;
      if (v>u && v<=start && D[v]>=0 && (D[u]<0 || D[v]+t<D[u]))
	D[u] = D[v]+t;
    }
  return D;
}

void precomp() {
  B = 2 * ((int)sqrt(N/K)+1) * K*K;
  for (int b=B; b<N; b+=B)
    for (int k=0; k<K && b+k<N; ++k)
      MidDist.push_back(dp_all_dist(b+k));
}

int dp_dist(int start, int dest) {
  vector<int> D(dest-start+1,-1);
  D[0] = 0;
  for (int u=start+1; u<=dest; ++u)
    for (const auto &e : G[u]) {
      int v = e._v_, t = e._t_;
      if (v<u && v>=start && D[v-start]>=0 &&
	  (D[u-start]<0 || D[v-start]+t<D[u-start]))
	D[u-start] = D[v-start]+t;
    }
  return D[dest-start];
}

int dist(int start, int dest) {
  int bs = start/B, bd = dest/B, dmin = -1;
  if (bs==bd) dmin = dp_dist(start,dest);
  else
    for (int k=0; k<K && bd*B+k<=dest; ++k) {
      int m = (bd-1)*K+k;
      if (MidDist[m][start]>=0 && MidDist[m][dest]>=0 &&
	  (dmin<0 || MidDist[m][start]+MidDist[m][dest]<dmin))
	dmin = MidDist[m][start]+MidDist[m][dest];
    }
  return dmin;
}

int main() {
  int M,O;
  cin >> K >> N >> M >> O;
  G.resize(N);
  for (int m=0; m<M; ++m) {
    int a,b,t;
    cin >> a >> b >> t; // b/K == 1 + a/K
    G[a].push_back(make_pair(b,t));
    G[b].push_back(make_pair(a,t));
  }
  precomp();
  for (int o=0; o<O; ++o) {
    int a,b;
    cin >> a >> b;
    cout << dist(a,b) << '\n';
  }
  return 0;
}
