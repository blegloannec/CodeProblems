#include <iostream>
#include <vector>
using namespace std;

int H,W;
vector< vector<char> > G;
vector< vector<int> > CC;

void dfs(int i, int j, int c) {
  CC[i][j] = c;
  vector< pair<int,int> > V {make_pair(i-1,j),make_pair(i+1,j),make_pair(i,j-1),make_pair(i,j+1)};
  for (auto iv=V.begin(); iv!=V.end(); ++iv) {
    int vi = iv->first, vj = iv->second;
    if (0<=vi && vi<H && 0<=vj && vj<W && G[i][j]==G[vi][vj] && CC[vi][vj]<0)
      dfs(vi,vj,c);
  }
}

int main() {
  cin >> H >> W;
  G.resize(H);
  CC.resize(H);
  for (int i=0; i<H; ++i) {
    G[i].resize(W);
    CC[i].resize(W,-1);
    for (int j=0; j<W; ++j)
      cin >> G[i][j];
  }
  int c = 0;
  for (int i=0; i<H; ++i)
    for (int j=0; j<W; ++j)
      if (CC[i][j]<0) {
	dfs(i,j,c);
	++c;
      }
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    int r1,c1,r2,c2;
    cin >> r1 >> c1 >> r2 >> c2;
    --r1; --c1; --r2; --c2;
    if (CC[r1][c1]==CC[r2][c2]) {
      if (G[r1][c1]=='1') cout << "decimal" << endl;
      else cout << "binary" << endl;
    }
    else cout << "neither" << endl;
  }
  return 0;
}
