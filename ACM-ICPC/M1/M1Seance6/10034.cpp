#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

#define MAX 100

struct edge {
  int ext1, ext2;
  double weight;
  edge(int e1, int e2, double w) : ext1(e1),ext2(e2),weight(w) {};
};

int size; // nombre de sommets
int tarj[MAX]; /* tableau pour Tarjan
		  t[i] = indice du pere de i */
vector<edge> edges; // liste des aretes

double vertices[MAX][2];

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
   
double kruskal() {
  init();
  // on trie les aretes
  sort(edges.begin(),edges.end(),inf);
  // glouton
  vector<edge>::iterator it = edges.begin();
  int c = 0;
  double res = 0;
  while (c<size-1) {
    if (find(it->ext1) != find(it->ext2)) {
      res += it->weight;
      fusion(it->ext1,it->ext2);
      ++c;
    }
    ++it;
  }
  return res;
}


int main() {
  int cas,n;
  cin >> cas;
  bool debut = true;
  while (cas-->0) {
    if (debut) debut = false;
    else cout << '\n';
    cin >> n;
    size = n;
    for (int i=0; i<n; ++i) {
      cin >> vertices[i][0] >> vertices[i][1];        
    }
    for (int i=0; i<n; ++i)
      for (int j=0; j<i; ++j)
        edges.push_back(edge(i,j,sqrt((vertices[i][0]-vertices[j][0])*
                             (vertices[i][0]-vertices[j][0])+
                             (vertices[i][1]-vertices[j][1])*
                             (vertices[i][1]-vertices[j][1]))));
    printf("%.2f\n",kruskal());    
    edges.clear();
  }
  return 0;
}
