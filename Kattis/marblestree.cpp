#include <iostream>
#include <vector>
using namespace std;

int N;
vector< vector<int> > T;
vector<int> M, Size;

int dfs_balance(int u) {
  int moves = 0;
  Size[u] = 1;
  for (int v : T[u]) {
    moves += dfs_balance(v);
    Size[u] += Size[v];
    M[u] += M[v];
  }
  // number of moves along the edge u -- parent(u)
  moves += abs(Size[u] - M[u]);
  return moves;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  while (true) {
    cin >> N;
    if (N<=0) break;
    T.resize(N);
    M.resize(N);
    /*
      /!\ Incredible BS: They give a *rooted* tree but do not specify
          the root, which is unfortunately not always the first vertex...
    */
    vector<bool> Root(N, true);
    for (int u=0; u<N; ++u) {
      int up1,d;
      cin >> up1 >> M[u] >> d;
      T[u].resize(d);
      for (int j=0; j<d; ++j) {
	cin >> T[u][j]; --T[u][j];
	Root[T[u][j]] = false;
      }
    }
    int root = 0;
    while (!Root[root]) ++root;
    Size.resize(N);
    cout << dfs_balance(root) << endl;
    // cleaning
    T.clear();
  }
  return 0;
}
