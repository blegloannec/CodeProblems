#include <iostream>
#include <vector>
#include <queue>
using namespace std;
using ll = long long;

#define _v_ first
#define _w_ second

#define _d_ first
#define _u_ second

const ll INF = 1LL<<60;
int N;
vector< vector< pair<int,ll> > > G;
vector<ll> Dist2Spid;

vector<ll> dijkstra(const vector<int> &U0, int uf=-1, ll dmin=0) {
  vector<ll> Dist(N, INF);
  priority_queue< pair<ll,int> > Q;
  for (int u : U0) {
    Dist[u] = 0;
    Q.push(make_pair(0,u));
  }
  while (!Q.empty()) {
    ll d = -Q.top()._d_; int u = Q.top()._u_;
    if (u==uf) break;
    Q.pop();
    if (Dist[u]<d) continue;
    for (const auto &e : G[u]) {
      int v = e._v_; ll w = e._w_;
      if (Dist2Spid[v]>=dmin && Dist[u]+w<Dist[v]) {
	Dist[v] = Dist[u] + w;
	Q.push(make_pair(-Dist[v], v));
      }
    }
  }
  return Dist;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int M; ll T;
  cin >> N >> M >> T;
  G.resize(N);
  for (int i=0; i<M; ++i) {
    int u,v; ll d;
    cin >> u >> v >> d;
    G[u].push_back(make_pair(v,d));
    G[v].push_back(make_pair(u,d));
  }
  int u0,uf;
  cin >> u0 >> uf;
  int K;
  cin >> K;
  vector<int> S(K);
  for (int i=0; i<K; ++i) cin >> S[i];
  // first pass of Dijkstra to compute the distances to spiders
  Dist2Spid.resize(N, INF);
  Dist2Spid = dijkstra(S);
  // dicho. search for the optimal distance to spiders
  // init. dr <= Dist2Spid[u0] is crucial as this is not verified
  // in the Dijkstra implem.
  vector<int> U0(1, u0);
  ll dl = 0, dr = min(Dist2Spid[u0], Dist2Spid[uf]);
  while (dl<dr) {
    ll d = (dl+dr+1)/2;
    // second pass of Dijkstra in the subgraph of vertices u
    // such that Dist2Spid[u] >= d
    ll t = dijkstra(U0, uf, d)[uf];
    if (t<=T) dl = d;
    else dr = d-1;
  }
  cout << dl << endl;
  return 0;
}
