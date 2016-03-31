struct edge {
  int ext1, ext2, weight;
  edge(int e1, int e2, int w) : ext1(e1),ext2(e2),weight(w) {};
};

int size; // nombre de sommets
int tarj[MAX]; /* tableau pour Tarjan
		  t[i] = indice du pere de i */
vector<edge> edges; // liste des aretes

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
      fusion(it->ext1,it->ext2);
      ++c;
    }
    ++it;
  }
  return res;
}
