// 20h45-21h22
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

#define MAX 3001

struct edge {
  int ext1, ext2, weight;
  edge(int e1, int e2, int w) : ext1(e1),ext2(e2),weight(w) {};
};

int size; // nombre de sommets
int tarj[MAX]; /* tableau pour Tarjan
		  t[i] = indice du pere de i */
vector<edge> edges; // liste des aretes

struct edge2 {
  int dest,weight;
  edge2(int d, int w) : dest(d), weight(w) {};
};

typedef vector<edge2> liste;

liste t[MAX]; // Table des listes de successeurs
int pred[MAX]; /* tableau des predecesseurs
		  A INITIALISER A -1 */
void clear_pred(int start) { // avant un DFS
  for (int i=0; i<size; ++i) pred[i] = -1;
  pred[start] = 0;
}


bool inf(edge a, edge b) { // ordre
  return (a.weight < b.weight);
}

void init() {
  for (int i=0; i<size; ++i)
    tarj[i] = -1;
}

int find(int e) { 
  // trouve le representant de la classe de e
  int p = tarj[e];
  if (p<0) return e;
  else {
    int root = find(p);
    tarj[e] = root; // pour aplatir l'arbre
    return root;
  }
}

void fusion(int a, int b) {
  // fusionne les classes de a et b
  tarj[find(b)] = find(a);
}
   
int kruskal() {
  init();
  // on trie les aretes
  sort(edges.begin(),edges.end(),inf);
  // glouton
  vector<edge>::iterator it = edges.begin();
  int c = 0;
  int res = 0;
  while (c<size-1) {
    if (find(it->ext1) != find(it->ext2)) {
      res += it->weight;
      t[it->ext1].push_back(edge2(it->ext2,it->weight));
      t[it->ext2].push_back(edge2(it->ext1,it->weight));
      fusion(it->ext1,it->ext2);
      ++c;
    }
    ++it;
  }
  return res;
}


// INITIALISER clear_pred(start);
bool DFS(int start, int dest) {
  // teste l'accessibilite de dest depuis start
  if (start==dest) return true; 
  liste::iterator it;
  for (it=t[start].begin(); it!=t[start].end(); ++it) {
    int d = it->dest;
    if (pred[d]<0) {
      pred[d] = max(pred[start],it->weight);
      if (DFS(d,dest)) return true;
    }
  }
  return false; 
}

int main() {
  int cas,N,R,a,b,l,Q;
  cin >> cas;
  for (int k=1; k<=cas; ++k) {
    cin >> N >> R;
    size = N;
    for (int i=0; i<R; ++i) {
      cin >> a >> b >> l;
      --a; --b;
      edges.push_back(edge(a,b,l));
    }
    kruskal();
    cin >> Q;
    cout << "Case " << k << '\n';
    for (int i=0; i<Q; ++i) {
      cin >> a >> b;
      --a; --b;
      clear_pred(a);
      DFS(a,b);
      cout << pred[b] << '\n';
    }
    edges.clear();
    for (int i=0; i<size; ++i) {
      t[i].clear();
    }
    cout << '\n';
  }

  return 0;
}
