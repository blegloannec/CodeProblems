#include <iostream>
#include <vector>
#include <deque>
using namespace std;

int main() {
  int H,W;
  cin >> H >> W;
  vector<string> G(H);
  for (int i=0; i<H; ++i) cin >> G[i];
  // init.
  deque< pair<int,int> > Q;
  vector< vector<int> > Dist(H, vector<int>(W, -1));
  vector< vector<bool> > Seen(H, vector<bool>(W, false));
  for (int i=0; i<H; ++i)
    for (int j=0; j<W; ++j)
      if (G[i][j]=='W') {
	Q.push_back(make_pair(i, j));
	Dist[i][j] = 0;
      }
  // BFS modified for 0-1 edges
  while (!Q.empty()) {
    auto ij = Q.front();
    Q.pop_front();
    int i = ij.first, j = ij.second;
    if (Seen[i][j]) continue;
    Seen[i][j] = true;
    for (int vi=i-1; vi<=i+1; ++vi)
      if (0<=vi && vi<H)
	for (int vj=j-1; vj<=j+1; ++vj)
	  if (0<=vj && vj<W) {
	    if (G[vi][vj]==G[i][j] && Dist[vi][vj]!=Dist[i][j]) {
	      // same connected region of a country
	      Dist[vi][vj] = Dist[i][j];
	      Q.push_front(make_pair(vi,vj));
	    }
	    else if (G[vi][vj]!=G[i][j] && Dist[vi][vj]<0) {
	      Dist[vi][vj] = Dist[i][j] + 1;
	      Q.push_back(make_pair(vi,vj));
	    }
	  }
  }
  // gathering results
  vector<int> L(26, -1);
  for (int i=0; i<H; ++i)
    for (int j=0; j<W; ++j)
      if (G[i][j]!='W') {
	int c = G[i][j] - 'A';
	if (L[c]<0 || Dist[i][j]<L[c])
	  L[c] = Dist[i][j];
      }
  // output
  for (int a=0; a<26; ++a)
    if (L[a]>0)
      cout << (char)(a+'A') << ' ' << L[a]-1 << endl;
  return 0;
}
