#include <iostream>
using namespace std;

#include <vector>
#include <queue>

#define MAX 100001


typedef vector<int> liste;
int size;
liste t[MAX]; // Tables des listes de successeurs
int pred[MAX]; /* tableau des predecesseurs
		  A INITIALISER A -1 */
int dist[MAX];

bool BFS(int start, int dest) {
  if (start==dest) return true; // RINN
  queue<int> q;
  int curr;
  liste::iterator it;
  q.push(start);
  pred[start] = start;
  dist[start] = 0;
  while (!q.empty()) {
    curr = q.front(); q.pop();
    for (it=t[curr].begin(); it!=t[curr].end(); ++it) {
      int d = *it;
      if (pred[d]<0) {
	q.push(d);
	pred[d] = curr;
	dist[d] = dist[curr]+1;
	if (d==dest) return true; // SINN
      }
    }
  }
  return false; // RINN
}


int main() {
  int cas,a,k,b;
  bool debut = true;
  cin >> cas;
  while (cas-->0) {
    if (debut) debut = false;
    else cout << '\n';
    cin >> size;
    for (int i=0; i<size; ++i) {
      cin >> a >> k;
      for (int j=0; j<k; ++j) {
	cin >> b;
	t[a].push_back(b);
	t[b].push_back(a);
      }
    }
    cin >> a >> b;
    for (int i=0; i<size; ++i) {
      pred[i] = -1;
      dist[i] = -1;
    }
    BFS(a,b);
    cout << a << ' ' << b << ' ' << dist[b]-1 << '\n';
    for (int i=0; i<size; ++i) t[i].clear();
  }
}
