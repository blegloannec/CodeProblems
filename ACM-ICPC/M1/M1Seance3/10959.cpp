#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>

using namespace std;

#define MAX 1001


typedef vector<int> liste;
int size;
liste t[MAX]; // Table des listes de successeurs
int pred[MAX]; /* tableau des predecesseurs
		  A INITIALISER A -1 */
void clear_pred(int start) { // avant un DFS
  for (int i=0; i<size; ++i) pred[i] = -1;
  pred[start] = 0;
}

void BFS(int start) {
  queue<int> q;
  int curr;
  liste::iterator it;
  clear_pred(start);
  q.push(start);
  while (!q.empty()) {
    curr = q.front(); q.pop();
    for (it=t[curr].begin(); it!=t[curr].end(); ++it) {
      int d = *it;
      if (pred[d]<0) {
	q.push(d);
	pred[d] = pred[curr] + 1;
      }
    }
  }
}

int main() {
  int cas,a,b,P,D;
  bool debut = true;
  cin >> cas;
  while (cas-->0) {
    if (debut) debut = false;
    else cout << '\n';
    cin >> P >> D;
    size = P;
    for (int i=0; i<D; ++i) {
      cin >> a >> b;
      t[a].push_back(b);
      t[b].push_back(a);
    }
    BFS(0);
    for (int i=0; i<P; ++i) {
      if (i>0) cout << pred[i] << '\n';
      t[i].clear();
    }
  }

  return 0;
}
