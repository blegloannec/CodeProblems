#include <iostream>
#include <vector>
#include <queue>
using namespace std;

typedef vector<int> liste;
#define MAX 100

liste pred[MAX];
liste succ[MAX];
queue<int> pending;
int nb_succ[MAX];
int dist[MAX]; // plus long chemin depuis un sommet
int end[MAX]; // dernier sommet d'un plus long chemin
int n;

int main() {
  int start,p,q;
  int cas = 1;
  while (cin >> n) {
    if (n==0) return 0;
    cin >> start;
    --start;

    // Init
    for (int i=0; i<n; ++i) {
      pred[i].clear();
      succ[i].clear();
      nb_succ[i] = 0;
      dist[i] = 0;
      end[i] = i;
    }

    while (cin >> p >> q) {
      if (p==0 && q==0) break;
      --p; --q;
      pred[q].push_back(p);
      succ[p].push_back(q);
      ++nb_succ[p];
    }
    
    for (int i=0; i<n; ++i) 
      if (nb_succ[i]==0)
	pending.push(i);
    
    while (!pending.empty()) {
      p = pending.front();
      pending.pop();
      
      for (int i=0; i<(int)pred[p].size(); ++i)
	if (--nb_succ[pred[p][i]] == 0)
	  pending.push(pred[p][i]);
    
      for (int i=0; i<(int)succ[p].size(); ++i)
	if (dist[p] < dist[succ[p][i]]+1) {
	  dist[p] = dist[succ[p][i]]+1;
	  end[p] = end[succ[p][i]];
	}
	else if (dist[p] == dist[succ[p][i]]+1)
	  if (end[p] > end[succ[p][i]])
	    end[p] = end[succ[p][i]];

      if (p == start)
	while (!pending.empty()) 
	  pending.pop();
    }

    
    cout << "Case " << cas++ << ": The longest path from " << start+1 << " has length " << dist[start] << ", finishing at " << end[start]+1 << ".\n\n";
    
  }
  return 0;
}
