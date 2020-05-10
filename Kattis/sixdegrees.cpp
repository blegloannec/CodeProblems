#include <iostream>
#include <vector>
#include <unordered_map>
#include <deque>
using namespace std;

int N;
vector< vector<int> > G;

bool bounded_bfs(int u0, int dmax=6) {
  vector<int> Dist(N,-1);
  Dist[u0] = 0;
  deque<int> Q;
  Q.push_back(u0);
  int cnt = 1;
  while (!Q.empty()) {
    int u = Q.front();
    Q.pop_front();
    for (int v : G[u])
      if (Dist[v]<0) {
	Dist[v] = Dist[u]+1;
	++cnt;
	if (Dist[v]<dmax) Q.push_back(v);
      }
  }
  return cnt==N;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    int M;
    cin >> M;
    N = 0;
    G.clear();
    unordered_map<string,int> Num;
    for (int i=0; i<M; ++i) {
      string su,sv;
      cin >> su >> sv;
      if (Num.find(su)==Num.end()) {
	Num[su] = N++;
	G.resize(N);
      }
      if (Num.find(sv)==Num.end()) {
	Num[sv] = N++;
	G.resize(N);
      }
      int u = Num[su], v = Num[sv];
      G[u].push_back(v);
      G[v].push_back(u);
    }
    int cnt = 0;
    for (int u=0; u<N; ++u)
      if (!bounded_bfs(u)) ++cnt;
    cout << (100*cnt<=5*N ? "YES" : "NO") << endl;
  }
  return 0;
}
