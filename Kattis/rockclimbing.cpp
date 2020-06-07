#include <iostream>
#include <vector>
using namespace std;

#define _i_ first
#define _j_ second

const int INF = 1<<30;

int H, W;
vector< vector<int> > X, E;

int dp_fixpt() {  // kinda custom bellman-ford from the end
  E.resize(1, vector<int>(W, 0));
  E.resize(H+2, vector<int>(W, INF));
  // E[i][j] = min energy to reach the top row from (i,j)
  bool unstable = true;
  while (unstable) {
    unstable = false;
    for (int i=1; i<=H+1; ++i)
      for (int j=0; j<W; ++j) {
	int e0 = E[i][j];
	vector< pair<int,int> > V
	  {make_pair(i+1,j), make_pair(i,j-1), make_pair(i,j+1), make_pair(i-1,j)};
	for (const auto &v : V)
	  if (0<=v._i_ && v._i_<=H+1 && 0<=v._j_ && v._j_<W && E[v._i_][v._j_]<INF)
	    E[i][j] = min(E[i][j], max(0, E[v._i_][v._j_] + X[i][j]));
	if (E[i][j]<e0) unstable = true;
      }
  }
  int res = INF;
  for (int j=0; j<W; ++j) res = min(res, E[H+1][j]);
  return res;
}

int main() {
  cin >> H >> W;
  for (int j=0; j<W; ++j) {  // E..E line
    char c;
    cin >> c;
  }
  X.resize(H+2, vector<int>(W, 0));
  for (int i=1; i<=H; ++i)
    for (int j=0; j<W; ++j)
      cin >> X[i][j];
  cout << dp_fixpt() << endl;
  return 0;
}
