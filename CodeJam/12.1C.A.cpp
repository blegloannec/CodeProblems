#include <iostream>
using namespace std;

#define NMAX 1000

int N;
bool G[NMAX][NMAX];
bool marque[NMAX];

bool DFS_cycle(int s0, int pred) {
  if (marque[s0]) return false;
  marque[s0] = true;
  for (int s=0; s<N; ++s)
    if (G[s0][s] && s!=pred)
      if (!DFS_cycle(s,s0))
	return false;
  return true;
}

int main() {
  int T,M,s0;
  bool test;
  cin >> T;
  for (int c=1; c<=T; ++c) {
    cin >> N;
    for (int i=0; i<N; ++i)
      for (int j=0; j<N; ++j)
	G[i][j] = false;
    for (int s=0; s<N; ++s) {
      cin >> M;
      for (int k=0; k<M; ++k) {
	cin >> s0;
	G[s0-1][s] = true;
      }
    }
    s0 = 0;
    test = true;
    while (test && s0<N) {
      for (int i=0; i<N; ++i)
	marque[i] = false;
      test = DFS_cycle(s0,-1);
      ++s0;
    }
    cout << "Case #" << c << ": " << (test?"No":"Yes") << endl;
  }
  return 0;
}
