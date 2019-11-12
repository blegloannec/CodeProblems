#include <iostream>
#include <vector>
#include <queue>
using namespace std;

const int INF = 1<<20;
int H,W,S,A,B,C,D;
string G;

vector<int> bfs(int u0) {  // bfs for a 0/1-weigth graph
  vector<int> V {-W,-1,1,W};
  vector<int> Dist(S, INF);
  Dist[u0] = G[u0]=='o';
  deque<int> Q;
  Q.push_back(u0);
  while (!Q.empty()) {
    int u = Q.front(); Q.pop_front();
    int ui = u/W, uj = u%W;
    for (int d : V) {
      int v = u+d;
      if (0<=v && v<S && G[v]!='#' && Dist[v]==INF && (v/W==ui || v%W==uj)) {
	int o = G[v]=='o';
	Dist[v] = Dist[u] + o;
	if (o) Q.push_back(v); // 1-edge
	else Q.push_front(v);  // trick for 0-edge
      }
    }
  }
  return Dist;
}

int main() {
  while (true) {
    cin >> W >> H;
    if (H==0) break;
    S = W*H;
    G.clear();
    for (int i=0; i<H; ++i) {
      string L;
      cin >> L;
      G += L;
    }
    for (int u=0; u<S; ++u)
      if      (G[u]=='A') A = u;
      else if (G[u]=='B') B = u;
      else if (G[u]=='C') C = u;
      else if (G[u]=='D') D = u;
    auto DistA = bfs(A), DistB = bfs(B), DistC = bfs(C), DistD = bfs(D);
    // O(S^2) search for the best structure
    int res = 1<<30;
    for (int E=0; E<S; ++E)
      if (G[E]!='#') {
	auto DistE = bfs(E);
	for (int F=E; F<S; ++F)
	  if (G[F]!='#') {
	    /*
	      E~F the common path
	      We try all combinations
	        A       C
	         \     /
	          E~~~F
	         /     \
	        B       D
	    */
	    int corr = 2*((G[E]=='o') + (G[F]=='o'));  // correction as E & F are counted 3 times each
	    res = min(res, DistA[E]+DistB[E] + DistE[F] + DistC[F]+DistD[F] - corr);
	    res = min(res, DistA[E]+DistC[E] + DistE[F] + DistB[F]+DistD[F] - corr);
	    res = min(res, DistA[E]+DistD[E] + DistE[F] + DistC[F]+DistB[F] - corr);
	    res = min(res, DistB[E]+DistC[E] + DistE[F] + DistA[F]+DistD[F] - corr);
	    res = min(res, DistB[E]+DistD[E] + DistE[F] + DistA[F]+DistC[F] - corr);
	    res = min(res, DistC[E]+DistD[E] + DistE[F] + DistA[F]+DistB[F] - corr);
	  }
      }
    cout << res << endl;
  }
  return 0;
}
