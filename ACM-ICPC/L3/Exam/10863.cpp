#include <iostream>
#include <vector>
#include <queue>
using namespace std;

const int INF = 1<<20;
int H, W, S, A[5];
vector<int> DistA[5], PredA[5];
string G;

void bfs(int u0, vector<int> &Dist, vector<int> &Pred) {  // bfs for a 0/1-weigth graph
  vector<int> V {-W,-1,1,W};
  Dist.resize(S);
  fill(Dist.begin(), Dist.end(), INF);
  Pred.resize(S);
  fill(Pred.begin(), Pred.end(), -1);
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
	Pred[v] = u;
	if (o) Q.push_back(v); // 1-edge
	else Q.push_front(v);  // trick for 0-edge
      }
    }
  }
}

vector<int> solution(int a, int b, int F, int c, int d) {
  const int e = 4;
  vector<int> sol;
  int u = A[e];
  while (u>=0) {
    if (G[u]=='o') sol.push_back(u);
    u = PredA[a][u];
  }
  u = A[e];
  while (u>=0) {
    if (G[u]=='o') sol.push_back(u);
    u = PredA[b][u];
  }
  u = F;
  while (u>=0) {
    if (G[u]=='o') sol.push_back(u);
    u = PredA[e][u];
  }
  u = F;
  while (u>=0) {
    if (G[u]=='o') sol.push_back(u);
    u = PredA[c][u];
  }
  u = F;
  while (u>=0) {
    if (G[u]=='o') sol.push_back(u);
    u = PredA[d][u];
  }
  return sol;
}

int main() {
  while (true) {
    cin >> W >> H;
    cout << W << ' ' << H << '\n';
    if (H==0) break;
    S = W*H;
    G.clear();
    for (int i=0; i<H; ++i) {
      string L;
      cin >> L;
      G += L;
    }
    for (int u=0; u<S; ++u)
      if ('A'<=G[u] && G[u]<='D')
	A[G[u]-'A'] = u;
    for (int i=0; i<4; ++i)
      bfs(A[i], DistA[i], PredA[i]);
    // O(S^2) search for the best structure
    int res = 1<<30;
    vector<int> best;
    for (int E=0; E<S; ++E)
      if (G[E]!='#') {
	A[4] = E;
	bfs(E, DistA[4], PredA[4]);
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
	    int distEF = DistA[4][F] - corr;
	    int d = DistA[0][E]+DistA[1][E] + distEF + DistA[2][F]+DistA[3][F];
	    if (d<res) {
	      res = d;
	      best = solution(0,1,F,2,3);
	    }
	    d = DistA[0][E]+DistA[2][E] + distEF + DistA[1][F]+DistA[3][F];
	    if (d<res) {
	      res = d;
	      best = solution(0,2,F,1,3);
	    }
	    d = DistA[0][E]+DistA[3][E] + distEF + DistA[1][F]+DistA[2][F];
	    if (d<res) {
	      res = d;
	      best = solution(0,3,F,1,2);
	    }
	    d = DistA[1][E]+DistA[2][E] + distEF + DistA[0][F]+DistA[3][F];
	    if (d<res) {
	      res = d;
	      best = solution(1,2,F,0,3);
	    }
	    d = DistA[1][E]+DistA[3][E] + distEF + DistA[0][F]+DistA[2][F];
	    if (d<res) {
	      res = d;
	      best = solution(1,3,F,0,2);
	    }
	    d = DistA[2][E]+DistA[3][E] + distEF + DistA[0][F]+DistA[1][F];
	    if (d<res) {
	      res = d;
	      best = solution(2,3,F,0,1);
	    }
	  }
      }
    for (int u : best) G[u] = '.';
    for (int i=0; i<H; ++i)
      cout << G.substr(i*W,W) << '\n';
    cout << '\n';
  }
  return 0;
}
